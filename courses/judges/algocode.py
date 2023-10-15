import requests
import json


def load_algocode_contest(contest, users):
    response = requests.get(contest.course.algocode_url)
    ext_standings_data = json.loads(response.text)

    users_map = {}
    for ext_user in ext_standings_data['users']:
        for user in users:
            if user.name.startswith(ext_user['name']):
                users_map[ext_user['id']] = user.id

    contest_data = None
    for ext_contest in ext_standings_data['contests']:
        if ext_contest['ejudge_id'] == contest.contest_id:
            contest_data = ext_contest
            break

    if contest_data is None:
        return None

    contest_data['id'] = contest.id

    user_info = {}
    for ext_uid, ext_user_info in contest_data['users'].items():
        ext_uid = int(ext_uid)
        if ext_uid not in users_map:
            continue
        local_uid = users_map[ext_uid]
        user_info[local_uid] = ext_user_info
    contest_data['users'] = user_info

    return contest_data

