import requests
import argparse
import os.path as op


class SearchRepo:

    def get(self, keyword, out):
        """The get method to search Github for the list of repositories

        Arguments:
        keyword -- the keyword to use for searching
        out -- the output file to be written in csv format
        """
        with open(op.abspath(out), 'w+', encoding="utf-8") as file:

            file.write('Name, Description, URL, Programming Language, Date of last update')

            page = 1
            while True:
                response = None
                try:
                    response = requests.get(
                        'https://api.github.com/search/repositories',
                        params={'q': f'{keyword}',
                                'page': page,
                                'per_page': 100
                                },
                    )
                except Exception as e:
                    print(e)
                    exit()

                # Check if the status of the response did not succeed and break the loop
                if response.status_code != 200:
                    print('Github API request limit exceeded!')
                    break

                json_response = response.json()

                # Check if the page consists of any item. Break the loop if it does not have any.
                if json_response['items']:
                    print(f'PAGE {page}: { len(json_response["items"]) } results')
                    for csv in json_response['items']:
                        file.write(f"\n{self.mdata_to_list(csv)}")
                else:
                    break

                page += 1

    @staticmethod
    def mdata_to_list(csv):
        """A separate function to format the line that will be written to the csv file

        Argument:
        csv -- the csv file path
        """

        name = f"\"{csv['full_name']}\""
        description = f"\"{csv['description']}\""
        url = f"\"{csv['html_url']}\""
        prog_lang = f"\"{csv['language']}\""
        dol_update = f"\"{csv['updated_at']}\""

        return f"{name}, {description}, {url}, {prog_lang}, {dol_update}"


if __name__ == "__main__":
    # The starting point of the script.
    # The code for the command line arguments

    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', help="the keyword to search",)
    parser.add_argument('out', help="the output csv file",)

    args = parser.parse_args()

    search = SearchRepo()
    search.get(args.keyword, args.out)
