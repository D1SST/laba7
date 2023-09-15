import itertools

class ApplicantDistributor:
    def __init__(self, women, men):
        self.women = women
        self.men = men
        self.options = []

    def distribute(self):
        self.options.clear()

        for women_option in itertools.combinations(self.women, 4):
            remaining_women = [w for w in self.women if w not in women_option]

            for men_option in itertools.combinations(self.men, 6):
                remaining_men = [m for m in self.men if m not in men_option]

                for women_option_specialty3 in itertools.combinations(remaining_women, 2):
                    remaining_women_specialty3 = [w for w in remaining_women if w not in women_option_specialty3]

                    for man_option_specialty3 in itertools.combinations(remaining_men, 1):
                        option = {
                            'Специальность 1 (women)': list(women_option),
                            'Специальность 2 (men)': list(men_option),
                            'Специальность 3': list(women_option_specialty3) + list(man_option_specialty3)
                        }

                        if 'W5' in option['Специальность 1 (women)'] or 'W6' in option['Специальность 1 (women)']:
                            continue

                        if len(option['Специальность 2 (men)']) < 4:
                            continue

                        self.options.append(option)

        for women_option in itertools.combinations(self.women, 4):
            remaining_women = [w for w in self.women if w not in women_option]

            for men_option in itertools.combinations(self.men, 6):
                remaining_men = [m for m in self.men if m not in men_option]

                for woman_option_specialty3 in itertools.combinations(remaining_women, 1):
                    remaining_women_specialty3 = [w for w in remaining_women if w != woman_option_specialty3[0]]

                    for men_option_specialty3 in itertools.combinations(remaining_men, 2):
                        option = {
                            'Специальность 1 (women)': list(women_option),
                            'Специальность 2 (men)': list(men_option),
                            'Специальность 3': list(woman_option_specialty3) + list(men_option_specialty3)
                        }

                        if 'W5' in option['Специальность 1 (women)'] or 'W6' in option['Специальность 1 (women)']:
                            continue

                        if len(option['Специальность 2 (men)']) < 4:
                            continue

                        self.options.append(option)

    def print_options(self):
        for i, option in enumerate(self.options, 1):
            print(f"Option {i}")
            for specialty, employees in option.items():
                print(f"{specialty}: {employees}")
            print()

women = ['W1', 'W2', 'W3', 'W4', 'W5', 'W6']
men = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8']

distributor = ApplicantDistributor(women, men)
distributor.distribute()
distributor.print_options()