#!/usr/bin/python
"""
Created on Tue Jun 2 20:14:43 2020

Universal Reddit Scraper 3.1.0.

@author: Joseph Lai
@contact: urs_project@protonmail.com
"""
import praw

from Credentials import API

from utils.Logger import LogMain
from utils.Tools import Run

class Main():
    """
    Run URS.
    """

    @staticmethod
    @LogMain.master_timer
    def main():
        reddit = praw.Reddit(
            client_id = API["client_id"],
            client_secret = API["client_secret"],
            user_agent = API["user_agent"],
            username = API["username"],
            password = API["password"])

        Run(reddit).run_urs()

if __name__ == "__main__":
    Main.main()
