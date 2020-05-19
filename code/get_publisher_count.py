#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2020,
# Daniele Cavestri <daniele.cavestri95@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.
import ast
import json as js
import requests
from os import sep


def make_requests(doi_file_name):
    # The txt file *doi_fil_name* is read to extract the list of dois. Moreover a set with all the unique prefixes of
    # the doi is created. Then for every prefix a query to http://api.crossref.org/prefixes/*prefix* is made with
    # requests.get(). At the end a dictionary with the following structure (and pseudocode notation) is created to store
    # all the data from the queries:
    # requests_dict = {'doi_1': {dict returned by requests.get('prefix_1')},
    # 'doi_2': {dict returned by requests.get('prefix_2')}, ...}
    #
    # The function returns requests_dict

    f = open(doi_file_name, "r")
    doi_list_str = f.read()
    doi_list = doi_list_str.split("\n")[:-1]

    #prefixes_set = set()
    #for doi in doi_list:
    #    curr_prefix = doi.split("/")[0]
    #    prefixes_set.add(curr_prefix)

    prefixes_set = {doi.split("/")[0] for doi in doi_list}

    prefixes_dict = dict()
    loading = 0
    total_loads = len(prefixes_set)
    for prefix in prefixes_set:
        loading += 1
        pretty_loading(loading, total_loads)
        r = requests.get("http://api.crossref.org/prefixes/" + prefix)
        bytes_data = r.content
        curr_dict_str = bytes_data.decode("UTF-8")
        try:
            curr_dict = ast.literal_eval(curr_dict_str)
            prefixes_dict[prefix] = curr_dict
        except (SyntaxError, ValueError, AssertionError):
            #SyntaxError, ValueError are for the literal_eval exceptions
            prefixes_dict[prefix] = dict()
            print("RISORSA NON TROVATAAAAAAA")
            pass

    #requests_dict = dict()
    #for doi in doi_list:
    #    curr_prefix = doi.split("/")[0]
    #    requests_dict[doi] = prefixes_dict[curr_prefix]

    requests_dict = {doi: prefixes_dict[doi.split("/")[0]] for doi in doi_list}

    return requests_dict


def pretty_loading(load_count, total_count):
    funny_loading_characters = ["|", "/", "-", "\\"]
    funny_char_selected = funny_loading_characters[load_count % 4]
    print("Loading ", funny_char_selected, " : ", load_count, " / ", total_count, " = ",
          round(100 * load_count / total_count, 1), "%")


def save_requests(requests_dict, out_file_name):
    # A json file with all the results from the queries made in make_requests() is saved
    json = js.dumps(requests_dict)
    f = open(out_file_name, "w")
    f.write(json)
    f.close()


def import_requests_results(file_name):
    # The json file previously saved is imported to avoid making queries with requests.get() on every execution
    with open(file_name, 'r') as fp:
        data = js.load(fp)
    return data


def count_editors(requests_dict):
    # A dictionary editors_dict is created and returned by the function. It contains the necessary information about
    # all the editors of the articles imported previously. It's structured as follows:
    # editors_dict = {'editor_1': {'count':*number of articles of editor_1*,
    # 'articles list':*list of articles of editor_1} , 'editor_2': {'count':*number of articles of editor_2*,
    # 'articles list':*list of articles of editor_2}, ...}
    editors_dict = dict()
    for doi in requests_dict:
        if requests_dict[doi]:
            curr_editor_name = requests_dict[doi]['message']['name']
            if curr_editor_name in editors_dict:
                editors_dict[curr_editor_name]['count'] += 1
                editors_dict[curr_editor_name]['articles list'].append(doi)
            else:
                editors_dict[curr_editor_name] = dict()
                editors_dict[curr_editor_name]['count'] = 1
                editors_dict[curr_editor_name]['articles list'] = list()
                editors_dict[curr_editor_name]['articles list'].append(doi)

    return editors_dict


def count_editors_test(requests_dict):
    doi_with_editor = [doi for doi in requests_dict if requests_dict[doi]]
    number_of_dois = len(doi_with_editor)

    editors_dict = count_editors(requests_dict)
    number_of_articles = 0
    for editor in editors_dict:
        number_of_articles += editors_dict[editor]['count']

    if number_of_dois == number_of_articles:
        print("TEST PASSED! :D")
    else:
        print("TEST FAILED! :'(")


#======================================== MAIN ========================================


doi_file_name = ".." + sep + "data" + sep + "dois_no_ref.csv"
requests_results_file_name = ".." + sep + "data" + sep + "article_publisher.json"

#requests_dict = make_requests(doi_file_name)
#save_requests(requests_dict, requests_results_file_name)
requests_dict = import_requests_results(requests_results_file_name)

editors_dict = count_editors(requests_dict)

count_editors_test(requests_dict)

