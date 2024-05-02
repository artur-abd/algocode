from django.core.management.base import BaseCommand

from courses.lib.mongo import mongo
from courses.models import Contest
from courses.judges import pcms

from courses.models import ContestStandingsHolder

import json


def upload_standings(contest, problems, runs_list):  # copy-paste from load_codeforces, refactor
    if not mongo.upload_standings(contest, [problems, runs_list]):
        try:
            standings_holder = contest.standings_holder.get()
        except:
            standings_holder = ContestStandingsHolder(contest=contest)
        standings_holder.problems = json.dumps(problems)
        standings_holder.runs_list = json.dumps(runs_list)
        standings_holder.save()


class Command(BaseCommand):
    help = 'Loads data for pcms standings'

    def handle(self, *args, **options):
        contests = Contest.objects.filter(judge=Contest.PCMS)
        users = dict()
        for contest in contests:
            print("loading", contest.external_group_id)
            try:
                problems, runs_list = pcms.load_pcms_contest(contest, users)
                if not mongo.upload_standings(contest, [problems, runs_list]):
                    upload_standings(contest, problems, runs_list)
                    # print("Can not upload standings to mongo")
            except Exception as e:
                print("Can not update contest, error:", e)
            except:
                print("Can not update contest, unknown error")

        print('PCMS loaded!')
