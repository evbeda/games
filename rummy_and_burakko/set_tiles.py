class SetTiles():
    def __init__(self, tiles):
        self.tiles = tiles.copy()

    # create an atribute containing the tiles
    def is_valid(self):
        return self.is_a_leg() or self.is_a_stair()

    def is_a_leg(self):
        colors = set([c.color for c in self.tiles])
        if len(colors) < 3 or len(colors) > 4:
            return False
        dif_color = len(colors) == len(self.tiles)
        # Evitamos que tomemos como ref a un joker
        for tile in self.tiles:
            if tile.number != 0:
                reference = tile.number
                break
        same_digit = all(
            obj.number == reference
            for obj in self.tiles
            if obj.is_joker is False
        )

        return dif_color and same_digit

    def is_a_stair(self):
        size = len(self.tiles)
        if size < 3 or size > 13:
            return False

        has_joker = False
        start = 0
        value_1 = self.tiles[start].get_number()
        if value_1 == 0:
            has_joker = True
            start = 1
            value_1 = self.tiles[start].get_number()
        color_ref = self.tiles[start].color

        for i in range(start + 1, size):
            value_2 = self.tiles[i].get_number()
            color = self.tiles[i].color
            # joker verification
            if value_2 == 0:
                if has_joker:
                    return False
                else:
                    has_joker = True
                    value_1 = value_1 + 1
                    continue
            # values and color verification
            if (value_2 == (value_1 + 1)) and color == color_ref:
                value_1 = value_2
                continue
            return False
        return True

    def remove_tile(self, tile):
        self.tiles.remove(tile)

    def get_tiles(self):
        set_type = ''
        if self.is_a_leg():
            set_type += 'L'
        elif self.is_a_stair():
            set_type += 'S'
        else:
            set_type += 'Wrong'
        return (
            set_type + '[ '
            + ' '.join([
                f'{index}:{tile.color}{tile.number}'
                for index, tile in enumerate(self.tiles)
            ])
            + ' ]'
        )

    def extract_one_tile(self, index):
        try:
            return self.tiles.pop(index)
        except IndexError:
            raise IndexError

    def put_tile(self, tile, index):
        if index < len(self.tiles):
            self.tiles.insert(index, tile)
        else:
            self.tiles.append(tile)

    def get_set_value(self):
        if self.is_a_leg():
            return self.leg_value()
        elif self.is_a_stair():
            return self.stair_value()
        else:
            return 0

    def leg_value(self):
        value = self.tiles[0].get_number()
        if value == 0:
            value = self.tiles[1].get_number()
        return value * len(self.tiles)

    def stair_value(self):
        q_tiles = len(self.tiles)
        start = self.tiles[0].get_number()
        end = start + q_tiles
        if start == 0:
            last_index = len(self.tiles) - 1
            end = self.tiles[last_index].get_number() + 1
            start = end - q_tiles

        return sum(list(range(start, end)))
