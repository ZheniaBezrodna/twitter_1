import urllib.request
import urllib.parse
import urllib.error
import twurl
import json
import ssl


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False


def input_value():
    # This function is for the user to be able to carry all the necessary data.

    users = input('Enter Twitter Account:')
    what_you_want = input('Enter what part of the file do you want to access. '
                          '\n' 'For example users:')
    entering = input('Enter the value you want to know about the user. \n'
                     'For example: id, id_str, name, location etc:')
    return check_value(users, what_you_want, entering)


def check_value(users, what_you_want, entering):
    # This function found and display specified information about users.

    """

    :param users: str, microsoft
    :param what_you_want: str, users
    :param entering: str, id
    :return: str, Your id of microsoft: 22028833
    """

    url = twurl.augment(TWITTER_URL, {'screen_name': users, 'count': '5'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    json_file = json.loads(data)
    if what_you_want not in json_file:
        print('Your entered data about what part of the file did you want to '
              'access did not found. '
              + '\n''One more time enter your data, please!')
        return input_value()
    for items in json_file[what_you_want]:
        if entering not in items:
            print('Your entered data for value about users did not found.'
                  + '\n''One more time enter your data, please!')
            return input_value()
        s = items[entering]
        return 'Your ' + str(entering) + ' of ' + users + ': ' + str(s)


if __name__ == "__main__":
    result = input_value()
    print result
