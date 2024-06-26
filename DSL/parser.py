class Parser:
    def __init__(self, lexer, fractal):
        self.lexer = lexer
        self.fractal = fractal
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception("Invalid syntax")

    def match(self, expected_token_type):
        if self.current_token.type == expected_token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def parse(self):
        self.parse_commands()

    def parse_commands(self):
        while self.current_token.type != "EOF":
            self.parse_command()

    def parse_command(self):
        command = self.current_token.value.lower()
        if command == 'size':
            self.match("SIZE")
            size_value = self.current_token.value
            self.match("NUMBER")
            self.fractal.set_size(int(size_value))
        elif command == 'color':
            self.match("COLOR")
            color_value = self.current_token.value
            self.match("STRING")
            self.fractal.set_color(color_value.strip("'").strip('"'))
        elif command == 'background':
            self.match("BACKGROUND")
            background_value = self.current_token.value
            self.match("STRING")
            self.fractal.set_background(background_value.strip("'").strip('"'))
        elif command == 'shape':
            self.match("SHAPE")
            shape_value = self.current_token.value
            self.match("STRING")
            self.fractal.set_shape(shape_value.strip("'").strip('"'))
        elif command == 'fill':
            self.match("FILL")
            fill_value = self.current_token.value
            self.match("STRING")
            self.fractal.set_fill(fill_value.strip("'").strip('"'))
        elif command == 'instant':
            self.match("INSTANT")
            instant_value = self.current_token.value
            self.match("STRING")
            self.fractal.set_instant(instant_value.strip("'").strip('"'))
        elif command == 'ratio':
            self.match("RATIO")
            ratio_value = self.current_token.value
            self.match("STRING")
            self.fractal.set_ratio(ratio_value.strip("'").strip('"'))
        elif command == 'speed':
            self.match("SPEED")
            speed_value = self.current_token.value
            self.match("NUMBER")
            self.fractal.set_speed(int(speed_value))
        elif command == 'depth':
            self.match("DEPTH")
            depth_value = self.current_token.value
            self.match("NUMBER")
            self.fractal.set_depth(int(depth_value))
        elif command == 'points':
            self.match("POINTS")
            points_value = self.current_token.value
            self.match("NUMBER")
            self.fractal.set_points_nr(int(points_value))
        elif command == 'length':
            self.match("LENGTH")
            length_value = self.current_token.value
            self.match("NUMBER")
            self.fractal.set_length(int(length_value))
        elif command == 'direction':
            self.match("DIRECTION")
            direction_value = self.current_token.value
            self.match("NUMBER")
            self.fractal.set_direction(int(direction_value))
        elif command == 'edges':
            self.match("EDGES")
            edges_value = self.current_token.value
            self.match("NUMBER")
            self.fractal.set_edges(int(edges_value))
        elif command == 'draw':
            self.match("DRAW")
            draw_value = self.current_token.value
            self.match("NUMBER")
            self.fractal.draw()
        else:
            self.error()
