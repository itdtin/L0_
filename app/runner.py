import copy
import pathlib
import random
import time
from pathlib import Path
import os

from queue import Queue
from web3 import Account, Web3
from logzero import logger
from app.helpers.utils import read_json, write_json

import config
import flows_config
from app.scripts import scripts


class Runner:

    def __init__(self, wallets_path):
        self.wallets = self.import_wallets(wallets_path)
        self.scripts = {func.__name__: func for func in scripts()}
        self.wallets_queue = Queue()
        for wallet in self.wallets:
            self.wallets_queue.put(wallet)
        self.results_path = pathlib.Path().resolve().joinpath("results.json")

        self.wait_wlt = (config.WAIT_BTW_WALLET_MIN, config.WAIT_BTW_WALLET_MAX)
        self.wait_projects = (config.WAIT_BTW_PROJECT_MIN, config.WAIT_BTW_PROJECT_MAX)

    def do_work(self):
        print("do work")

        while self.wallets_queue.qsize():
            wallet = self.wallets_queue.get()
            print(f"Running on the wallet: {wallet.address}")
            self.run_projects_in_order(wallet)
            self.make_pause_btw_wlt()

    def run_projects_in_order(self, wallet):
        previous_flow_result = True
        json_results = read_json(self.results_path)
        results_for_wallet = json_results.get(wallet.address, {})
        random_order = copy.copy(config.to_random_run)
        random.shuffle(random_order)
        logger.info(random_order)
        for project_name in random_order:
            project_actions = flows_config.PROJECTS[project_name]
            results_for_project = results_for_wallet.get(project_name, {})
            for action_params in project_actions:
                script_name = action_params['script']
                action_name = f"{script_name}_{action_params['srcToken']}_{action_params['srcChain']}_{action_params['dstToken']}_{action_params['dstChain']}"
                project_title = f"{project_name}_{action_name}"
                key = "swap" if "swap" in script_name else "bridge"
                if config.to_run[project_name].get(key):
                    if previous_flow_result and not results_for_project.get(action_name, False):
                        logger.info(f"RUNNUNIG {project_title} ...")
                        flow_result = self.run_project(wallet, action_params)
                        results_for_project[action_name] = flow_result
                        results_for_wallet[project_name] = results_for_project
                        previous_flow_result = flow_result
                        self.make_pause_btw_projects()
        json_results[wallet.address] = results_for_wallet
        write_json(self.results_path, json_results)

    def run_project(self, wallet, run_args=None):
        try:
            if not run_args:
                run_args = {}
            args = [wallet] + [run_args]
            flow_ = self.scripts.get(run_args["script"])
            if flow_:
                return flow_(*args)
        except:
            return False

    def import_wallets(self, file_name: str):
        accounts = []
        if os.path.exists(file_name):
            with Path(file_name).open() as file:
                for line in file.readlines():
                    key_ = line.replace("\n", "")
                    try:
                        acc = Account.from_key(key_)
                        accounts.append(acc)
                    except Exception as e:
                        logger.error("ERROR| Incorrect PK")
            if len(accounts) > 0:
                logger.info("INFO | Wallets has been loaded")
            return accounts
        else:
            logger.error(" ERROR | Incorrect path to wallets.txt")
        return []

    def make_pause_btw_wlt(self) -> None:
        self.make_pause(self.wait_wlt)

    def make_pause_btw_projects(self) -> None:
        self.make_pause(self.wait_projects)

    @staticmethod
    def make_pause(wait_type):
        counter = random.randint(*wait_type)
        logger.info(f"INFO | Pause ...{counter}... seconds")
        step = 1
        while counter > 0:
            time.sleep(step)
            counter -= step
