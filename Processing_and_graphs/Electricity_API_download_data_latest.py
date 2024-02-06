# start by downloading the package
# pip install deutschland
# poetry add deutschland -E smard

#import package
from deutschland import smard

import pandas as pd

from deutschland.smard import Configuration
from deutschland.smard.api_client import ApiClient
from deutschland.smard.api_client import Endpoint as _Endpoint
from deutschland.smard.model.indices import Indices
from deutschland.smard.model.time_series import TimeSeries

class DownloadAPI(object):
    """
    DownloadAPI is a class to download data from https://smard.de/app API, which enables us to download data about: 
    electrity generation from different sources (nuclear energy, offshore wind, onshore wind, hydropower, biomas, natural gas, photovoltaics, coal...), 
    consumption (total, residual load, pumped storage),
    market spot prices (DE, BE, AT, NO, DK, FR, NL, PL, CH, SI, CZ, HU)
    and forecast generation (onshore, photovoltaics, wind and photocoltaics, total). 
    It downloads the data based on inputed parameters for specific filter, region, resultion and timestamp, converts it into nice clean Pandas DataFrame.
    The first part of the code was inspired by github repository https://github.com/bundesAPI/smard-api/tree/main. Changes were made to make the code work for our project. 
    ....
    Attributes
    ----------
    api_client 
        It is part of ApiClient class from deutschlad.smard library, it enables the API. 
    
    chart_data_chart_data_API_request_endpoint
        Used to make requests to API endpoint in order to get specific time series data. 
        It is a part of "_Endpoint" class from deutschland.smard library.       
    ....
    Methods
    ----------
    def __init__()
        It initializes the class. In case that api_client is not provided it creates ApiClient by default. 
    
    def chart_data_API_request()
        It makes API request based on the specified endpoint, filters, regions and timestamps.
        Parameters:
            filter(int)
            filter_copy(int) - same as filter(), it must be filled due to wrong API design from creators
            region(str) - defaultly set as DE
            region_copy(str) - same as region(), it must be filled due to wrong API design from creators
            timestamp(integer)
            resolution(str)
            **kwargs

    def chart_data_timestamps()
        Returns available timestamps based on the combination of filter, region and resolution.         
        Parameters:
            filter(int)
            region(str) - defaultly set as DE
            timestamp(integer)
            resolution(str)
            **kwargs

    def download_chart_data()
        Downloads the data and returns it as a Pandas DataFrame. It also converts the timestamp column into normal date. 
        Parameters:
            Same as for the method chart_data_API_request(). 

    def simplifier_filter():
        Getting the filter number based on insert name.
        Parameters: 
            filter_word(str)
        
    def simplifier_filter_copy():
        Getting the filter_copy number based on inserted filter name.
        Parameters: 
            filter_word_copy(str)

    def download_chart_data_by_name()
        Calls both simplifiers and connects it with download_chart_data function, making the whole process more user friendly. 
        One must be careful while typing the name of the filter, it must match with keys in the dictionary_filters. 
        Parameters: 
            filter_word(str) 
            filter_word_copy(str)
            region(str), 
            region_copy(str),
            timestamp(int)
            resolution(str) 
            **kwargs    
    """
    def __init__(self, api_client=None):
        """
        Initiator. It defines the endpoint. 
        """
        #when api_client is not defined, it creates APIClient 
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        print(api_client.configuration.host)
        #definition of endpoint
        self.chart_data_API_request_endpoint = _Endpoint(
            settings={
                "response_type": (TimeSeries,),
                "auth": [],
                "endpoint_path": "/chart_data/{filter}/{region}/{filterCopy}_{regionCopy}_{resolution}_{timestamp}.json",
                "operation_id": "chart_data_API_request",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["filter","filter_copy","region","region_copy","resolution","timestamp",],
                "required": ["filter","filter_copy","region","region_copy","resolution","timestamp",],
                "nullable": [],
                "enum": ["filter","filter_copy","region","region_copy","resolution",],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("filter",): { "1223": 1223,"1224": 1224,"1225": 1225,"1226": 1226,"1227": 1227,"1228": 1228,"4066": 4066,"4067": 4067,"4068": 4068,"4069": 4069,"4070": 4070,
                        "4071": 4071,"410": 410,"4359": 4359,"4387": 4387,"4169": 4169,"5078": 5078,"4996": 4996,"4997": 4997,"4170": 4170,"252": 252,"253": 253,"254": 254,
                        "255": 255,"256": 256,"257": 257,"258": 258,"259": 259,"260": 260,"261": 261,"262": 262,"3791": 3791,"123": 123,"126": 126,"715": 715,"5097": 5097,"122": 122,
                    },
                    ("filter_copy",): {"1223": 1223,"1224": 1224,"1225": 1225,"1226": 1226,"1227": 1227,"1228": 1228,"4066": 4066,"4067": 4067,"4068": 4068,"4069": 4069,"4070": 4070,
                        "4071": 4071,"410": 410,"4359": 4359,"4387": 4387,"4169": 4169,"5078": 5078,"4996": 4996,"4997": 4997,"4170": 4170,"252": 252,"253": 253,"254": 254,
                        "255": 255,"256": 256,"257": 257,"258": 258,"259": 259,"260": 260,"261": 261,"262": 262,"3791": 3791,"123": 123,"126": 126,"715": 715,"5097": 5097,"122": 122,
                    },
                    ("region",): {"DE": "DE","AT": "AT","LU": "LU","DE-LU": "DE-LU","DE-AT-LU": "DE-AT-LU","50HERTZ": "50Hertz","AMPRION": "Amprion","TENNET": "TenneT","TRANSNETBW": "TransnetBW","APG": "APG","CREOS": "Creos",
                    },
                    ("region_copy",): {"DE": "DE","AT": "AT","LU": "LU","DE-LU": "DE-LU","DE-AT-LU": "DE-AT-LU","50HERTZ": "50Hertz","AMPRION": "Amprion","TENNET": "TenneT","TRANSNETBW": "TransnetBW","APG": "APG","CREOS": "Creos",
                    },
                    ("resolution",): {"HOUR": "hour","QUARTERHOUR": "quarterhour","DAY": "day","WEEK": "week","MONTH": "month","YEAR": "year",
                    },
                },
                "openapi_types": {"filter": (int,),"filter_copy": (int,),"region": (str,),"region_copy": (str,),"resolution": (str,),"timestamp": (int,),},
                "attribute_map": {"filter": "filter","filter_copy": "filterCopy","region": "region","region_copy": "regionCopy","resolution": "resolution","timestamp": "timestamp",},
                "location_map": {"filter": "path","filter_copy": "path","region": "path","region_copy": "path","resolution": "path","timestamp": "path",},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.chart_data_timestamps_endpoint = _Endpoint(
            settings={
                "response_type": (Indices,),
                "auth": [],
                "endpoint_path": "/chart_data/{filter}/{region}/index_{resolution}.json",
                "operation_id": "chart_data_timestamps",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["filter","region","resolution",],
                "required": ["filter","region","resolution",],
                "nullable": [],
                "enum": ["filter","region","resolution",],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("filter",): {"1223": 1223,"1224": 1224,"1225": 1225,"1226": 1226,"1227": 1227,"1228": 1228,"4066": 4066,"4067": 4067,"4068": 4068,"4069": 4069,"4070": 4070,
                        "4071": 4071,"410": 410,"4359": 4359,"4387": 4387,"4169": 4169,"5078": 5078,"4996": 4996,"4997": 4997,"4170": 4170,"252": 252,"253": 253,"254": 254,
                        "255": 255,"256": 256,"257": 257,"258": 258,"259": 259,"260": 260,"261": 261,"262": 262,"3791": 3791,"123": 123,"126": 126,"715": 715,"5097": 5097,"122": 122,                        
                    },
                    ("region",): {"DE": "DE","AT": "AT","LU": "LU","DE-LU": "DE-LU","DE-AT-LU": "DE-AT-LU","50HERTZ": "50Hertz","AMPRION": "Amprion","TENNET": "TenneT","TRANSNETBW": "TransnetBW","APG": "APG","CREOS": "Creos",
                    },
                    ("resolution",): {"HOUR": "hour","QUARTERHOUR": "quarterhour","DAY": "day","WEEK": "week","MONTH": "month","YEAR": "year",
                    },
                },
                "openapi_types": {"filter": (int,),"region": (str,),"resolution": (str,),},
                "attribute_map": {"filter": "filter","region": "region","resolution": "resolution",},
                "location_map": {"filter": "path","region": "path","resolution": "path",},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        
    def chart_data_API_request(self,filter,filter_copy,region_copy,timestamp,region="DE",resolution="day",**kwargs):
        """
        This method creates an API request. 

        Parameters:
            filter(int)
                 `1223` - Electricity generation: Brown coal (Lignite)
                 `1224` - Electricity generation: Nuclear energy
                 `1225` - Electricity generation: Offshore wind
                 `1226` - Electricity generation: Hydropower
                 `1227` - Electricity generation: Other Conventional
                 `1228` - Electricity generation: Other renewables
                 `4066` - Electricity generation: Biomass
                 `4067` - Electricity generation: Onshore wind, 
                 `4068` - Electricity generation: Photovoltaics
                 `4069` - Electricity generation: Hard coal
                 `4070` - Electricity generation: Pumped storage
                 `4071` - Electricity generation: Natural gas, 
                 `410` - Electricity consumption: Total (grid load)
                 `4359` - Electricity consumption: Residual load
                 `4387` - Electricity consumption: Pumped storage, 
                 `4169` - Market price: Germany/Luxembourg
                 `5078` - Market price: neighbors DE/LU
                 `4996` - Market price: Belgium
                 `4997` - Market price: Norway 2, 
                 `4170` - Market price: Austria
                 `252` - Market price: Denmark 1
                 `253` - Market price: Denmark 2
                 `254` - Market price: France
                 `255` - Market price: Italy (North), 
                 `256` - Market price: Netherlands
                 `257` - Market price: Poland
                 `258` - Market price: Poland
                 `259` - Market price: Switzerland
                 `260` - Market price: Slovenia, 
                 `261` - Market price: Czech Republic
                 `262` - Market price: Hungary
                 `3791` - Forecasted generation: Offshore
                 `123` - Forecast generation: Onshore 
                 `125` - Forecast generation: Photovoltaic
                 `715` - Forecast generation: Other
                 `5097` - Forecast generation: Wind and photovoltaic
                 `122` - Forecast generation: Total
            filter_copy(int) - same as filter(), it must be filled due to wrong API design from creators
            region(str) - defaultly set as "DE"
            region_copy(str) - same as region(), it must be filled due to wrong API design from creators
            timestamp(integer)
            resolution(str) - resolution of the data, defaultly as "hour"   
                `hour` - Hourly, `quarterhour` - Quarterhourly, `day` - Daily, `weekly` - Weekly, `monthly` - Monthly, `yearly` - Yearly
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
        kwargs["filter"] = filter
        kwargs["filter_copy"] = filter_copy
        kwargs["region"] = region
        kwargs["region_copy"] = region_copy
        kwargs["resolution"] = resolution
        kwargs["timestamp"] = timestamp
        return self.chart_data_API_request_endpoint.call_with_http_info(
            **kwargs)
       
    def chart_data_timestamps(self, filter, region, resolution, **kwargs):
        """
        Returns available timestamps based on the combination of filter, region and resolution. 
        Parametrs same as in 'chart_data_API_request()'

        Returns:
            Indices
                If the method is called asynchronously, returns the request thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["filter"] = filter
        kwargs["region"] = region
        kwargs["resolution"] = resolution
        return self.chart_data_timestamps_endpoint.call_with_http_info(
            **kwargs)

    def download_chart_data(self, filter, filter_copy, region, region_copy, timestamp=None, resolution="day" , **kwargs):
        """
        Gets all available timestamps based on given arguments. Using for loop it downloads coresponding data, transforms the timestamp into date and appends it to the list. 
        Then it concatenates the all the data into one merged data frame. Furthermore, it processes the data by dropping NAs, sorting by the date and renaming the columns.  

        Returns:
            If the data was successfully downloaded a DataFrame is returned. Otherwise - None. 
        """
        try:
            # Get all available timestamps for a given combination of arguments at once 
            timestamps_response = self.chart_data_timestamps(filter, region, resolution, **kwargs)
            timestamps = timestamps_response.get('timestamps', [])
            # Download data for each timestamp using for loop 
                #creating an empty list for storage of dataframes
            list_dfs = []
                #for loop -getting data for each timestamp 
            for timestamp in timestamps:
                #API request
                response = self.chart_data_API_request(
                    filter, filter_copy, region_copy, timestamp, region, resolution, **kwargs
                )
                #processing the API response 
                json_response = eval(response.to_str())
                series_data = json_response.get('series', [])
                df = pd.DataFrame(series_data, columns=['timestamp', 'value'])
                # Convert timestamp to date
                df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
                df['date'] = df['timestamp'].dt.date
                #append to the list
                list_dfs.append(df)

            # All timestamps into one Dataframe using concatenate function 
            merged_df = pd.concat(list_dfs, ignore_index=True)

            # Additional changes - to make the final DataFrame look nicer 
            final_df = merged_df.sort_values(by="date")
            final_df = merged_df.reset_index(drop="True")

                #1 Filtering out rows where 'values' is not Null or NaN/NA
            final_df_clean = final_df[final_df['value'].notna()]
                #2 Finding the last date with a non-null or non-NA/Nan value
            last_date_with_value = final_df_clean['date'].max()
            last_date_with_value = last_date_with_value.strftime('%Y-%m-%d')
            print("Our last available data are form:", last_date_with_value)
                #3 Erasing rows for which we don't have a value Value
            final_df_clean.loc[:, 'date'] = final_df_clean['date'].astype(str)
            final_df_clean = final_df_clean[final_df_clean['date'] <= last_date_with_value]
            del final_df_clean['date']
                #4 Convert the 'timestamp' column to datetime and extract date part only 
            final_df_clean['timestamp'] = pd.to_datetime(final_df_clean['timestamp']).dt.date
                #6 Renaming the columns
            final_df_clean.rename(columns={'timestamp': 'Date', 'value': 'Values'}, inplace=True)

            return final_df_clean
        except Exception as e:
            print("Something went wrong while downloading or processing the data into Pandas Dataframe. Please check your previous steps.")
            print(e)
            return None
        
    dictionary_filters = {
        'el_gen_brown_coal':1223, 'el_gen_nuclear_energy':1224, 'generation off shore wind':1225,
        'el_gen_hydropower':1226, 'generation from other convential sources':1227,
        'generation from other renewables':1228, 'el_gen_biomas':4066, 'generation on shore wind':4067,
        'generation from photovoltaics':4068, 'el_gen_hard_coal':4069, 'generation from pumper storage':4070,
        'el_gen_natural_gas':4071,'el_cons_total_gid':410, 'el_cons_res_grid':4359,
        'el_cons_pumped_storage':4387, 'market_price_de_lux':4169, 'market_price_neighbors_de_lux':5078,
        'market_price_be':4996,'market_price_no':4997, 'market_price_at':4170, 'market_price_dk_1':252,
        'market_price_dk_2':253, 'market_price_it':255, 'market_price_fr':254, 'market_price_nt':256,
        'market_price_pl_1':257,'market_price_pl_2':258, 'market_price_ch':259, 'market_price_si':260,
        'market_price_cz':261, 'market_price_hu':262,'forecast_gen_off':3791, 'forecast_gen_on':123,
        'forecast_gen_photovoltaic':125, 'forecast_gen_other':715, 'forecast_gen_wind_photo':5097,
        'forecast_total':122, 'total electricity consumption' : 410
    }

    def simplifier_filter(self,filter_word):
        """
        Getting the filter number based on insert name.
        """
        return self.dictionary_filters.get(filter_word.lower().strip())

    def simplifier_filter_copy(self,filter_word_copy):
        """
        Getting the filter_copy number based on inserted filter name.
        """
        return self.dictionary_filters.get(filter_word_copy.lower().strip())

    def download_chart_data_by_name(self,filter_word, filter_word_copy,region, region_copy, timestamp=None, resolution="day" , **kwargs):
        """
        Calls both simplifiers and connects it with download_chart_data function, making the whole process more user friendly. 
        One must be careful while typing the name of the filter, it must match with keys in the dictionary_filters. 

        Returs:
        DataFrame using the function download_chart_data. 
        """
        filter_num= self.simplifier_filter(filter_word)
        filter_num_copy= self.simplifier_filter_copy(filter_word_copy)
        if filter_num is None or filter_num_copy is None:
            print(f"Typo in filter name -> unknown filter: {filter_word}")
            return None
        return self.download_chart_data(filter_num, filter_num_copy,region, region_copy, timestamp=None, resolution="day" , **kwargs)

    

#config = Configuration(host="https://www.smard.de/app", discard_unknown_keys=True)
#api_client = ApiClient(config)
#download_api = DownloadAPI(api_client)

#downloading example data 
#Elect_gen_onshore_wind = download_api.download_chart_data(filter=4067, filter_copy=4067,region="DE", region_copy="DE")
#print(Elect_gen_onshore_wind)

#API_values = download_api.download_chart_data_by_name(filter_word="Generation from photovoltaics", filter_word_copy="Generation from photovoltaics", region="DE", region_copy="DE")
#API_values.to_csv('C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Processing_and_graphs/API_values.csv', index = False, encoding='windows-1252')
#print(API_values)

# Variables of interest:
# 1125: Generation off shore wind
# 1127: Generation from other convential sources
# 1128: Generation from other renewables
# 4067: Generation on shore wind
# 4068: Generation from photovoltaics
# 4070: Generation from pumper storage
# 410: Total electricity consumption


