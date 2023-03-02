import unittest
import requests

url = 'http://127.0.0.1:8000'

class TestMain(unittest.TestCase):


    def setUp(self):
        self.game_db = {
            "Name": "Game",
            "StudioName": "Studio"
        }
    
    # POST
    def test_add_game(self):
        response = requests.post(url + '/game', json=self.game_db)
        self.assertEqual(response.status_code, 200)
        game = response.json()
        self.assertEqual(game['Name'], self.game_db['Name'])
        self.assertEqual(game['StudioName'], self.game_db['StudioName'])


    # PUT
    def test_update_game_by_id(self):
        response = requests.get(url + '/game')
        game = response.json()
        for i in range(0, len(game["data"])):
            if game["data"][i]["Name"] == "Game":
                id = game["data"][i]["id"]
                break

        mock = {
            "Name": "Test",
            "StudioName": "Test"
        }

        response = requests.put(url + f'/games/{id}', json=mock)
        self.assertEqual(response.status_code, 200)
        mock_json = response.json()
        
        self.assertEqual(mock_json['Name'], mock['Name'])
        self.assertEqual(mock_json['StudioName'], mock['StudioName'])


    #  GET list
    def test_get_games(self):
        response = requests.get(url + '/games')
        self.assertEqual(response.status_code, 200)
        games = response.json()["data"]
        self.assertIsInstance(games, list)
        self.assertGreater(len(games), 0)
        game = games[0]
        self.assertIsInstance(game, dict)
        self.assertIn("id", game)
        self.assertIsInstance(game["id"], int)
        self.assertIn("Name", game)
        self.assertIsInstance(game["Name"], str)
        self.assertIn("StudioName", game)
        self.assertIsInstance(game["StudioName"], str)


    # GET
    def test_get_game_by_id(self):
        response = requests.get(url + '/game')
        game = response.json()
        for i in range(0, len(game["data"])):
            if game["data"][i]["Name"] == "Test":
                id = game["data"][i]["id"]
                break

        response = requests.get(url + f'/game/{id}')
        self.assertEqual(response.status_code, 200)
        game = response.json()
        self.assertIsInstance(game, dict)
        self.assertIn("id", game)
        self.assertIsInstance(game["id"], int)
        self.assertIn("Name", game)
        self.assertIsInstance(game["Name"], str)
        self.assertIn("StudioName", game)
        self.assertIsInstance(game["StudioName"], str)


    # Check endpoint: delete a game from the database
    def test_delete_game_by_id(self):
        response = requests.get(url + '/games')
        game = response.json()
        for i in range(0, len(game["data"])):
            if game["data"][i]["Name"] == "Test":
                id = game["data"][i]["id"]
                break

        response = requests.delete(url + f'/games/{id}')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
