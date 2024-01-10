import os
from notion_client import Client
from pprint import pprint
import streamlit as st
from dataclasses import dataclass
# from config.static import STATUS_ICON
from collections import namedtuple
from datetime import datetime
from zoneinfo import ZoneInfo

# TTL = 24 * 60 * 60


@dataclass
class Challenges:
    id: str
    icon: str
    name: str
    status: str
    category: str
    type: str
    stack: []
    start_date: str
    end_date: str
    page_url: str


STATUS_ICON = {
    "Initiation": "💡",
    "Waiting List": "➕",
    "Drafting": "✍",
    "Ready to Launch": "🚀",
    "Published": "🌏",
    "Archived": "📑"
}


CHALLENGE = namedtuple(
    "Challenge",
    ["id", "icon", "name", "status", "category", "type",
        "stack", "start_date", "end_date", "page_url"]
)

# @st.cache_data(ttl=TTL, show_spinner="Fetching roadmap...")


def _get_raw_data(
    auth=st.secrets.notion_client.NOTION_AUTH,
    database_id=st.secrets.notion_client.DB_ID
):
    """_summary_

    Parameters
    ----------
    auth : _type_, optional
        _description_, by default st.secrets.notion_client.NOTION_AUTH
    database_id : _type_, optional
        _description_, by default st.secrets.notion_client.DB_ID

    Returns
    -------
    _type_
        _description_
    """

    notion = Client(auth=auth)
    db_query = notion.databases.query(
        database_id=database_id,
        filter={
            "property": "Share to Web Page",
            "checkbox": {"equals": True},
        },
    )
    return db_query


def get_tech_stack(stack_props):
    """_summary_

    Parameters
    ----------
    stack_props : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    return [stack['name'] for stack in stack_props]


def get_page_name(name_props):
    """_summary_

    Parameters
    ----------
    name_props : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    return "".join(name["plain_text"] for name in name_props)


def challenge_status_pair(status_props):
    """_summary_

    Parameters
    ----------
    status_data : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    icon = ""
    for key, value in STATUS_ICON.items():
        if key == status_props:
            icon = value
    return f"{icon} {status_props}"


def format_date(date_props):
    """_summary_

    Parameters
    ----------
    date_props : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    # parse the datetime string
    # remove the milliseconds and timezone offset
    dt = datetime.fromisoformat(date_props[:-6])

    # create a timezone object for the given offset
    # use the 'Etc/GMT+/-HH' format to specify the timezone offset
    tz = ZoneInfo('Etc/GMT+7')

    # convert the datetime object to the desired timezone
    dt = dt.replace(tzinfo=tz)

    # format the datetime object
    fmt = '%B %d, %Y %H:%M'
    dt_fmt = dt.strftime(fmt)

    # return the formatted datetime string
    return dt_fmt


def query_base_info(props):
    """_summary_

    Parameters
    ----------
    props : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """

    all_challenges = []

    for result in props:
        raw_data = result['properties']

        challenge_id = result['id']
        challenge_icon = result['icon']['emoji']
        challenge_name = get_page_name(raw_data['Name']['title'])
        challenge_status = challenge_status_pair(
            raw_data['Status']['status']['name'])
        challenge_category = raw_data['Challenge Category']['select']['name']
        challenge_type = raw_data['Challenge Type']['select']['name']
        challenge_stack = get_tech_stack(
            raw_data['Tech Stack']['multi_select'])
        challenge_start_date = format_date(
            raw_data['Timeline']['date']['start'])
        challenge_end_date = format_date(raw_data['Timeline']['date']['end'])
        challenge_page = result['public_url']

        challenges_data = Challenges(
            id=challenge_id,
            icon=challenge_icon,
            name=challenge_name,
            status=challenge_status,
            category=challenge_category,
            type=challenge_type,
            stack=challenge_stack,
            start_date=challenge_start_date,
            end_date=challenge_end_date,
            page_url=challenge_page
        )
        all_challenges.append(challenges_data)

    return all_challenges


def clean_data():
    props = _get_raw_data()["results"]
    base_info = query_base_info(props)
    pprint(base_info)
