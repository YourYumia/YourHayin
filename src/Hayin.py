class Character:
    def __init__(self):
        self.username = input("What is your name? ")
        self.attributes = [
            {
                "name": "Keyo",
                "total": 0.0,
                "elements": [0.0, 0.0, 0.0],  # illio[0], anemo[1], dendro[2]
            },
            {
                "name": "Dara",
                "total": 0.0,
                "elements": [0.0, 0.0, 0.0],  # paega[0], gaia[1], fulma[2]
            },
        ]

    # return polarity as str by default; returns the polarity as a dict if internal_call = 0
    def get_polarity(self, internal_call=0) -> any:
        return (
            "Keyo"
            if self.attributes[0]["total"] > self.attributes[1]["total"]
            else "Dara",
            self.attributes[0]
            if self.attributes[0]["total"] > self.attributes[1]["total"]
            else self.attributes[1],
        )[internal_call]

    # return aligned element as str
    def get_alignment(self) -> "str":
        polarity = self.get_polarity(1)
        ali_index = 0

        for i in range(0, len(polarity["elements"])):
            if i == ali_index:
                continue
            
            ali_index = (
                i
                if polarity["elements"][i] > polarity["elements"][ali_index]
                else ali_index
            )

        for i in range(len(polarity["elements"])):
            if (
                i != ali_index
                and polarity["elements"][i] == polarity["elements"][ali_index]
            ):  # some overlap is accounted for via combination elements
                selection = [ali_index, i]

                match selection:
                    case [0, 1] | [1, 0]:
                        return "Illemo" if polarity["name"] == "Keyo" else "Pegaia"
                    case [0, 2] | [2, 0]:
                        return "Denillio" if polarity["name"] == "Keyo" else "Fulpaega"
                    case [1, 2] | [2, 1]:
                        return "Anendro" if polarity["name"] == "Keyo" else "Fulgaia"

            # will run if a combination element isn't present
            return (
                ["Illio", "Anemo", "Dendro"][ali_index]
                if polarity["name"] == "Keyo"
                else ["Paega", "Gaia", "Fulma"][ali_index]
            )

    def update_attr(self, polarity_i: int, element_i: int, amount: float) -> None:
        if amount != 0.0:  # don't recalculate if nothing will actually change
            self.attributes[polarity_i]["elements"][element_i] += amount
            for attribute in self.attributes:
                attribute["total"] = sum(attribute["elements"])


class QuizEntry:
    def __init__(self, config: dict):
        self.question = config["input str"]
        self.target = [
            config["polarity index"],  # [0] (keyo) / [1] (dara)
            config["alignment index"],  # [0] / [1] / [2]
        ]