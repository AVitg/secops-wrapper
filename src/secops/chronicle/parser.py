#
"""Parser functionality for Chronicle."""

from typing import Dict, Any, List, Optional
from datetime import datetime
from secops.exceptions import APIError
from secops.chronicle.models import CaseList, Case, SoarPlatformInfo


def _get_parser(client, parser) -> str:
    
    #url = f"https://{cli_region.lower()}-chronicle.googleapis.com/v1alpha/projects/{PROJECT_ID}/locations/{cli_region.lower()}/instances/{CUSTOMER_ID}/logTypes/{logtype.upper()}/parsers"

    url = f"{client.base_url}/{client.instance_id}/logTypes/{parser}/parsers"
    response = client.session.get(url)
    
    if response.status_code != 200:
        raise APIError(f"Failed to get parser: {response.text}")
    
    # Parse the response
    response_data = response.json()    
   
    return response_data 


def _get_parser_with_id(client, parser, parser_id) -> str:
    """Get parser from Chronicle.
    
    Args:
        client: ChronicleClient instance
        parser: parser to retrieve
        
    Returns:
       parser

    Raises:
    """
    # Check that we don't exceed the maximum number of cases
    
    url = f"{client.base_url}/{client.instance_id}/logTypes/{parser}/parsers/{parser_id}"
        
    response = client.session.get(url)
    
    if response.status_code != 200:
        raise APIError(f"Failed to get parser: {response.text}")
    
    # Parse the response
    response_data = response.json()
    
   
    return response_data
