#importing packages
import pandas as pd
import numpy as np
from zipfile import ZipFile
import requests

from deutschland.smard import Configuration
from deutschland.smard.api_client import ApiClient
from deutschland.smard.api_client import Endpoint as _Endpoint
from deutschland.smard.model.time_series import TimeSeries
from deutschland.smard.model_utils import (
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)

class DownloadAPI(object):
    """
    DownloadAPI is a class to download data from https://smard.de/app API, which enables us to download data about: 
    electrity generation from different sources (nuclear energy, offshore wind, onshore wind, hydropower, biomas, natural gas, photovoltaics, coal...), 
    consumption (total, residual load, pumped storage),
    market spot prices (DE, BE, AT, NO, DK, FR, NL, PL, CH, SI, CZ, HU)
    and forecast generation (onshore, photovoltaics, wind and photocoltaics, total). 
    It downloads the data based on inputed parameters for specific filter, region, resultion and timestamp. 

    ....

    Attributes
    ----------
    api_client 
        It is part of ApiClient class from deutschlad.smard library, it enables the API. 
    
    chart_data_filter_region_filter_copy_resolution_timestamp_json_get_endpoint
        Used to make requests to API endpoint in order to get specific time series data. 
        It is a part of "_Endpoint" class from deutschland.smard library.       

    ....

    Methods
    ----------
    def __init__()
        It initializes the class. In case that api_client is not provided it creates ApiClient by default. 
    
    def chart_data_filter_region_filter_copy_region_copy_resolution_timestamp_json_get()
        It makes API request based on the specified endpoint, filters, regions and timestamps.
        Parameters:
            filter(int)
            filter_copy(int) - same as filter(), it must be filled due to wrong API design from creators
            region(str) - defaultly set as DE
            region_copy(str) - same as region(), it must be filled due to wrong API design from creators
            timestamp(integer)
            resolution(str)
            **kwargs
        
    def download_chart_data()
        Makes an API request, downloads the data and saves it as Panda DataFrame.
        Parameters:
            Same as previous method chart_data_filter_region_filter_copy_region_copy_resolution_timestamp_json_get(). 
    
    """
    def __init__(self, api_client=None):
        #when api_client is not defined, it creates APIClient 
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        print(api_client.configuration.host)
        #definition of endpoint
        self.chart_data_filter_region_filter_copy_region_copy_resolution_timestamp_json_get_endpoint = _Endpoint(
            settings={
                "response_type": (TimeSeries,),
                "auth": [],
                "endpoint_path": "/chart_data/{filter}/{region}/{filterCopy}_{regionCopy}_{resolution}_{timestamp}.json",
                "operation_id": "chart_data_filter_region_filter_copy_region_copy_resolution_timestamp_json_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "filter",
                    "filter_copy",
                    "region",
                    "region_copy",
                    "resolution",
                    "timestamp",
                ],
                "required": [
                    "filter",
                    "filter_copy",
                    "region",
                    "region_copy",
                    "resolution",
                    "timestamp",
                ],
                "nullable": [],
                "enum": [
                    "filter",
                    "filter_copy",
                    "region",
                    "region_copy",
                    "resolution",
                ],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("filter",): {
                        "1223": 1223,
                        "1224": 1224,
                        "1225": 1225,
                        "1226": 1226,
                        "1227": 1227,
                        "1228": 1228,
                        "4066": 4066,
                        "4067": 4067,
                        "4068": 4068,
                        "4069": 4069,
                        "4070": 4070,
                        "4071": 4071,
                        "410": 410,
                        "4359": 4359,
                        "4387": 4387,
                        "4169": 4169,
                        "5078": 5078,
                        "4996": 4996,
                        "4997": 4997,
                        "4170": 4170,
                        "252": 252,
                        "253": 253,
                        "254": 254,
                        "255": 255,
                        "256": 256,
                        "257": 257,
                        "258": 258,
                        "259": 259,
                        "260": 260,
                        "261": 261,
                        "262": 262,
                        "3791": 3791,
                        "123": 123,
                        "126": 126,
                        "715": 715,
                        "5097": 5097,
                        "122": 122,
                    },
                    ("filter_copy",): {
                        "1223": 1223,
                        "1224": 1224,
                        "1225": 1225,
                        "1226": 1226,
                        "1227": 1227,
                        "1228": 1228,
                        "4066": 4066,
                        "4067": 4067,
                        "4068": 4068,
                        "4069": 4069,
                        "4070": 4070,
                        "4071": 4071,
                        "410": 410,
                        "4359": 4359,
                        "4387": 4387,
                        "4169": 4169,
                        "5078": 5078,
                        "4996": 4996,
                        "4997": 4997,
                        "4170": 4170,
                        "252": 252,
                        "253": 253,
                        "254": 254,
                        "255": 255,
                        "256": 256,
                        "257": 257,
                        "258": 258,
                        "259": 259,
                        "260": 260,
                        "261": 261,
                        "262": 262,
                        "3791": 3791,
                        "123": 123,
                        "126": 126,
                        "715": 715,
                        "5097": 5097,
                        "122": 122,
                    },
                    ("region",): {
                        "DE": "DE",
                        "AT": "AT",
                        "LU": "LU",
                        "DE-LU": "DE-LU",
                        "DE-AT-LU": "DE-AT-LU",
                        "50HERTZ": "50Hertz",
                        "AMPRION": "Amprion",
                        "TENNET": "TenneT",
                        "TRANSNETBW": "TransnetBW",
                        "APG": "APG",
                        "CREOS": "Creos",
                    },
                    ("region_copy",): {
                        "DE": "DE",
                        "AT": "AT",
                        "LU": "LU",
                        "DE-LU": "DE-LU",
                        "DE-AT-LU": "DE-AT-LU",
                        "50HERTZ": "50Hertz",
                        "AMPRION": "Amprion",
                        "TENNET": "TenneT",
                        "TRANSNETBW": "TransnetBW",
                        "APG": "APG",
                        "CREOS": "Creos",
                    },
                    ("resolution",): {
                        "HOUR": "hour",
                        "QUARTERHOUR": "quarterhour",
                        "DAY": "day",
                        "WEEK": "week",
                        "MONTH": "month",
                        "YEAR": "year",
                    },
                },
                "openapi_types": {
                    "filter": (int,),
                    "filter_copy": (int,),
                    "region": (str,),
                    "region_copy": (str,),
                    "resolution": (str,),
                    "timestamp": (int,),
                },
                "attribute_map": {
                    "filter": "filter",
                    "filter_copy": "filterCopy",
                    "region": "region",
                    "region_copy": "regionCopy",
                    "resolution": "resolution",
                    "timestamp": "timestamp",
                },
                "location_map": {
                    "filter": "path",
                    "filter_copy": "path",
                    "region": "path",
                    "region_copy": "path",
                    "resolution": "path",
                    "timestamp": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,)
        
    def chart_data_filter_region_filter_copy_region_copy_resolution_timestamp_json_get(
        self,
        filter,
        filter_copy,
        region_copy,
        timestamp,
        region="DE",
        resolution="day",
        **kwargs
    ):
        """
        It makes API request based on the specified endpoint, filters, regions and timestamps.  This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request: pass async_req=True. 
        >>> thread = api.chart_data_filter_region_filter_copy_region_copy_resolution_timestamp_json_get(filter, filter_copy, region_copy, timestamp, region="DE", resolution="hour", async_req=True)
        >>> result = thread.get()
        
        Parameters:
            filter(int)
                 * `1223` - Electricity generation: Brown coal (Lignite) 
                 * `1224` - Electricity generation: Nuclear energy
                 * `1225` - Electricity generation: Offshore wind   
                 * `1226` - Electricity generation: Hydropower   
                 * `1227` - Electricity generation: Other Conventional   
                 * `1228` - Electricity generation: Other renewables   
                 * `4066` - Electricity generation: Biomass   
                 * `4067` - Electricity generation: Onshore wind   
                 * `4068` - Electricity generation: Photovoltaics   
                 * `4069` - Electricity generation: Hard coal   
                 * `4070` - Electricity generation: Pumped storage   
                 * `4071` - Electricity generation: Natural gas
                 * `410` - Electricity consumption: Total (grid load)   
                 * `4359` - Electricity consumption: Residual load   
                 * `4387` - Electricity consumption: Pumped storage   
                 * `4169` - Market price: Germany/Luxembourg   
                 * `5078` - Market price: neighbors DE/LU   
                 * `4996` - Market price: Belgium   
                 * `4997` - Market price: Norway 2   
                 * `4170` - Market price: Austria   
                 * `252` - Market price: Denmark 1   
                 * `253` - Market price: Denmark 2   
                 * `254` - Market price: France   
                 * `255` - Market price: Italy (North)   
                 * `256` - Market price: Netherlands   
                 * `257` - Market price: Poland   
                 * `258` - Market price: Poland   
                 * `259` - Market price: Switzerland  
                 * `260` - Market price: Slovenia   
                 * `261` - Market price: Czech Republic   
                 * `262` - Market price: Hungary
                 * `3791` - Forecasted generation: Offshore   
                 * `123` - Forecast generation: Onshore   
                 * `125` - Forecast generation: Photovoltaic   
                 * `715` - Forecast generation: Other   
                 * `5097` - Forecast generation: Wind and photovoltaic   
                 * `122` - Forecast generation: Total
            filter_copy(int) - same as filter(), it must be filled due to wrong API design from creators
            region(str) - defaultly set as "DE"
                Land / Regelzone / Marktgebiet:   
                * `DE` - Land: Deutschland   
                * `AT` - Land: Österreich   
                * `LU` - Land: Luxemburg   
                * `DE-LU` - Marktgebiet: DE/LU (ab 01.10.2018)   
                * `DE-AT-LU` - Marktgebiet: DE/AT/LU (bis 30.09.2018)   
                * `50Hertz` - Regelzone (DE): 50Hertz   
                * `Amprion`- Regelzone (DE): Amprion   
                * `TenneT` - Regelzone (DE): TenneT   
                * `TransnetBW` - Regelzone (DE): TransnetBW   
                * `APG` - Regelzone (AT): APG   
                * `Creos` - Regelzone (LU): Creos 
            region_copy(str) - same as region(), it must be filled due to wrong API design from creators
            timestamp(integer)
            resolution(str) - resolution of the data, defaultly as "hour"   
                * `hour` - Hourly 
                * `quarterhour` - Quarterhourly 
                * `day` - Daily 
                * `weekly` - Weekly 
                * `monthly` - Monthly 
                * `yearly` - Yearly
            **kwargs
        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            A timeseries object representing the data.
            If the method is called asynchronously, returns the request thread.
        """
        #optional parametrs 
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        # kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["filter"] = filter
        kwargs["filter_copy"] = filter_copy
        kwargs["region"] = region
        kwargs["region_copy"] = region_copy
        kwargs["resolution"] = resolution
        kwargs["timestamp"] = timestamp
        return self.chart_data_filter_region_filter_copy_region_copy_resolution_timestamp_json_get_endpoint.call_with_http_info(
            **kwargs)
    
    def download_chart_data(self, filter, filter_copy, region_copy, timestamp, region="DE", resolution="day", **kwargs):
        """
        Download the data and return it as a Pandas DataFrame.
        Returns:
            If the data was successfully downloaded a DataFrame is returned. Otherwise - None. 
        """
        try:
            # API request
            response = self.chart_data_filter_region_filter_copy_region_copy_resolution_timestamp_json_get(
                filter, filter_copy, region_copy, timestamp, region, resolution, **kwargs
            )

            # Process the API response
            json_data_dic = eval(response.to_str())
            series_data = json_data_dic.get('series', [])
            df = pd.DataFrame(series_data, columns=['timestamp', 'value'])
            
            return df
        except Exception as e:
            print("Something went wrong while downloading or processing the data. Please check your previous steps.")
            print(e)
            return None


config = Configuration(host="https://www.smard.de/app", discard_unknown_keys=True)
api_client = ApiClient(config)
download_api = DownloadAPI(api_client)

df = download_api.download_chart_data(filter=1223, filter_copy=1223, region_copy="DE", timestamp=1672527600000)
if df is not None:
    # Now you have the DataFrame for further processing
    print(df.head())
