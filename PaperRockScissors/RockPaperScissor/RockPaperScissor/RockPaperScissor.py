import time
import random


class game:
    def __init__(self):
        # set the seed.
        random.seed(time.strftime("%H%M%S"))

    def __update_gamer_score(self):
        """
        Adding a single point to gamer score.
        """
        self.game["gamer_score"] = self.game["gamer_score"] + 1

    def __update_pc_score(self):
        """
        Adding a single point to pc score.
        """
        self.game["pc_score"] = self.game["pc_score"] + 1

    def start_the_game(self):
        """
        The game function defines a signle game. The move of the gamer is given as input
        while the move of the pc is based on the extraction of a random number.
        """
        # save each steps of the game.
        self.game = {}
        self.game["gamer_score"] = 0
        self.game["pc_score"] = 0

        # Insert the number of matches.
        while True:
            try:
                self.total_matches = int(input("Number of matches: "))
                break
            except ValueError:
                print("The input number isn't correct. Retry.")

        #
        count = 0

        while count < self.total_matches:
            print(f"\n ----- ROUND NUMBER: {count + 1}")

            # check my move.
            while True:
                try:
                    gamer_move = input("Your move: ")
                    if gamer_move not in ["Scissor", "Rock", "Paper"]:
                        raise ValueError("")
                    break  # serve per uscire dal while se l'except non occorre.
                except ValueError:
                    print(f"Unknown move. Retry or you will lose.")

            # computer move.
            r = random.random()
            if 0 <= r <= 1 / 3:
                pc_move = "Scissor"
            elif 1 / 3 <= r <= 2 / 3:
                pc_move = "Rock"
            else:
                pc_move = "Paper"

            if gamer_move == pc_move:
                print("You drew: retry")
            else:
                if (gamer_move == "Paper") | (pc_move == "Paper"):
                    if (gamer_move == "Scissor") | (pc_move == "Scissor"):
                        if gamer_move == "Scissor":
                            self.__update_gamer_score()
                        else:
                            self.__update_pc_score()

                    if (gamer_move == "Rock") | (pc_move == "Rock"):
                        if gamer_move == "Rock":
                            self.__update_pc_score()
                        else:
                            self.__update_gamer_score()

                if (gamer_move == "Rock") | (pc_move == "Rock"):
                    if (gamer_move == "Scissor") | (pc_move == "Scissor"):
                        if gamer_move == "Scissor":
                            self.__update_pc_score()
                        else:
                            self.__update_gamer_score()
                print(
                    f"My score: {self.game['gamer_score']} vs. PC score: {self.game['pc_score']}"
                )
                count = count + 1

            print(f"----- MY GAME: {gamer_move} vs. PC MOVE: {pc_move}")
        print("\n\n\n***-------- THE END --------***")
        if self.game["gamer_score"] > self.game["pc_score"]:
            winner = "You"
        else:
            winner = "PC"
        print(
            f"My score: {self.game['gamer_score']} vs. PC score: {self.game['pc_score']} ---> {winner}"
        )
