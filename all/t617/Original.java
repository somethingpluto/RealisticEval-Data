 // this entire method was written by chatgpt because I HATE IT
    public static void initialReadFromJSON() throws Exception {
        JSONParser parser = new JSONParser();
        FileReader reader = new FileReader("src/main/resources/usersJSON.json");
        JSONObject jo = (JSONObject) parser.parse(reader);

        JSONArray usersArray = (JSONArray) jo.get("users");
        for (Object userObj : usersArray) {
            JSONObject userJSON = (JSONObject) userObj;
            String username = (String) userJSON.get("username");
            String password = (String) userJSON.get("password");

            JSONArray gamesArray = (JSONArray) userJSON.get("games");
            ArrayList<Game> games = new ArrayList<>();
            for (Object gameObj : gamesArray) {
                JSONObject gameJSON = (JSONObject) gameObj;
                String name = (String) gameJSON.get("name");
                String genre = (String) gameJSON.get("genre");
                String desc = (String) gameJSON.get("desc");
                int year = ((Long) gameJSON.get("year")).intValue();
                String imagePath = (String) gameJSON.get("img");

                games.add(new Game(name, genre, desc, year, imagePath));
            }

            users.add(new User(username, password, games));
        }

        reader.close();
    }
