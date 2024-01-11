import os
from notion_client import Client
import streamlit as st
from dataclasses import dataclass, field, asdict
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import List, Dict, Optional
from backend.static import STATUS_ICON


# TTL = 24 * 60 * 60


@dataclass
class Challenges:
    id: str = None
    name: str = None
    status: str = None
    category: str = None
    type: str = None
    stack: List[str] = None
    start_date: str = None
    end_date: str = None
    page_url: str = None
    
    def _to_dict(self) -> Dict:
        return {k: v for k, v in asdict(self).items()}
        


# @st.cache_data(ttl=TTL, show_spinner="Fetching roadmap...")
def _get_raw_data(
    auth=st.secrets.notion_client.NOTION_AUTH,
    database_id=st.secrets.notion_client.DB_ID
) -> List:
    """Request gallery data on Notion

    Parameters
    ----------
    auth : optional
        Notion Auth for integrations, by default st.secrets.notion_client.NOTION_AUTH
    database_id : optional
        Targetted Database in Notion, by default st.secrets.notion_client.DB_ID

    Returns
    -------
    List
        Return all data that checked for "Share to Web Page"
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


def get_tech_stack(stack_props) -> List:
    """Append tech stack from Tech Stack data

    Parameters
    ----------
    stack_props : dict
        The raw tech stack data based on request

    Returns
    -------
    List
        Return clean tech stack information
    """
    return [stack['name'] for stack in stack_props]


def complete_page_name(icon_props, name_props) -> str:
    """Retrieve page content name from request

    Parameters
    ----------
    name_props : dict
        The raw page name based on request

    Returns
    -------
    str
        Return page name
    """
    return "".join(name["plain_text"] for name in name_props)


def challenge_status_pair(status_props):
    """Pairing challenges with great icons

    Parameters
    ----------
    status_props : dict
        The raw status date based on request

    Returns
    -------
    str
        Return paired of icon and statu name
    """
    icon = ""
    for key, value in STATUS_ICON.items():
        if key == status_props:
            icon = value
    return f"{icon} {status_props}"


def format_date(date_props):
    """Formatting date like notion creation

    Parameters
    ----------
    date_props : dict
        The raw date data based on request

    Returns
    -------
    str
        Return formatted date
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


def query_base_info(props) -> List:
    """Construct the request date to Challenges class

    Parameters
    ----------
    props : List
        The Raw Request Data

    Returns
    -------
    List
        Return list of clean Challenges data
    """

    all_challenges = []
    
    for result in props:
        raw_data = result['properties']

        challenge_id = result['id']
        challenge_name = complete_page_name(icon_props=result['icon']['emoji'], name_props=raw_data['Name']['title'])
        challenge_status = challenge_status_pair(raw_data['Status']['status']['name'])
        challenge_category = raw_data['Challenge Category']['select']['name']
        challenge_type = raw_data['Challenge Type']['select']['name']
        challenge_stack = get_tech_stack(raw_data['Tech Stack']['multi_select'])
        challenge_start_date = format_date(raw_data['Timeline']['date']['start'])
        challenge_end_date = format_date(raw_data['Timeline']['date']['end'])
        challenge_page = result['public_url']

        challenges_data = Challenges(
            id=challenge_id,
            name=challenge_name,
            status=challenge_status,
            category=challenge_category,
            type=challenge_type,
            stack=challenge_stack,
            start_date=challenge_start_date,
            end_date=challenge_end_date,
            page_url=challenge_page
        )._to_dict()
        
        all_challenges.append(challenges_data)

    return all_challenges


def clean_data():
    props = _get_raw_data()["results"]
    base_info = query_base_info(props)
    return props, base_info