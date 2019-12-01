class JogoDaVelha:
    def __init__(self):
        self.iniciar_jogo()

    def iniciar_jogo(self):
        self.estado_atual = [['.', '.', '.'],
                             ['.', '.', '.'],
                             ['.', '.', '.']]

        self.player_turn = 'X'

    def desenhar(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.estado_atual[i][j]), end=" ")
            print()
        print()

    def valido(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.estado_atual[px][py] != '.':
            return False
        else:
            return True

    def final(self):
        for i in range(0, 3):
            if (self.estado_atual[0][i] != '.' and
                self.estado_atual[0][i] == self.estado_atual[1][i] and
                    self.estado_atual[1][i] == self.estado_atual[2][i]):
                return self.estado_atual[0][i]

        for i in range(0, 3):
            if (self.estado_atual[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.estado_atual[i] == ['O', 'O', 'O']):
                return 'O'

        if (self.estado_atual[0][0] != '.' and
            self.estado_atual[0][0] == self.estado_atual[1][1] and
                self.estado_atual[0][0] == self.estado_atual[2][2]):
            return self.estado_atual[0][0]

        if (self.estado_atual[0][2] != '.' and
            self.estado_atual[0][2] == self.estado_atual[1][1] and
                self.estado_atual[0][2] == self.estado_atual[2][0]):
            return self.estado_atual[0][2]

        for i in range(0, 3):
            for j in range(0, 3):
                if (self.estado_atual[i][j] == '.'):
                    return None

        return '.'

    def max(self):
        mxv = -2

        px = None
        py = None

        resultado = self.final()

        if resultado == 'X':
            return (-1, 0, 0)
        elif resultado == 'O':
            return (1, 0, 0)
        elif resultado == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.estado_atual[i][j] == '.':
                    self.estado_atual[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    if m > mxv:
                        mxv = m
                        px = i
                        py = j
                    self.estado_atual[i][j] = '.'
        return (mxv, px, py)

    def min(self):
        minv = 2

        qx = None
        qy = None

        resultado = self.final()

        if resultado == 'X':
            return (-1, 0, 0)
        elif resultado == 'O':
            return (1, 0, 0)
        elif resultado == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.estado_atual[i][j] == '.':
                    self.estado_atual[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.estado_atual[i][j] = '.'

        return (minv, qx, qy)

    def mx_alpha_beta(self, alpha, beta):
        mxv = -2
        px = None
        py = None

        resultado = self.final()

        if resultado == 'X':
            return (-1, 0, 0)
        elif resultado == 'O':
            return (1, 0, 0)
        elif resultado == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.estado_atual[i][j] == '.':
                    self.estado_atual[i][j] = 'O'
                    (m, min_i, in_j) = self.mn_alpha_beta(alpha, beta)
                    if m > mxv:
                        mxv = m
                        px = i
                        py = j
                    self.estado_atual[i][j] = '.'
                    if mxv >= beta:
                        return (mxv, px, py)

                    if mxv > alpha:
                        alpha = mxv

        return (mxv, px, py)

    def mn_alpha_beta(self, alpha, beta):

        minv = 2

        qx = None
        qy = None

        resultado = self.final()

        if resultado == 'X':
            return (-1, 0, 0)
        elif resultado == 'O':
            return (1, 0, 0)
        elif resultado == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.estado_atual[i][j] == '.':
                    self.estado_atual[i][j] = 'X'
                    (m, max_i, max_j) = self.mx_alpha_beta(alpha, beta)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.estado_atual[i][j] = '.'

                    if minv <= alpha:
                        return (minv, qx, qy)

                    if minv < beta:
                        beta = minv

        return (minv, qx, qy)

    def run(self):

        while True:
            self.desenhar()
            self.resultado = self.final()

            if self.resultado != None:
                if self.resultado == 'X':
                    print('O X é o ganhador!')
                elif self.resultado == 'O':
                    print('O 0 é o ganhador')
                elif self.resultado == '.':
                    print("Empatou!")

                self.iniciar_jogo()
                return

            if self.player_turn == 'X':

                while True:
                    (m, qx, qy) = self.mn_alpha_beta(-2, 2)
                    px = int(input('Insira a coordenada X : '))
                    py = int(input('Insira a coordenada Y: '))

                    qx = px
                    qy = py

                    if self.valido(px, py):
                        self.estado_atual[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print(
                            'Movimento inválido, entre com as coodenadas X e Y novamente.')

            else:
                (m, px, py) = self.mx_alpha_beta(-2, 2)
                self.estado_atual[px][py] = 'O'
                self.player_turn = 'X'


if __name__ == "__main__":
    g = JogoDaVelha()
    g.run()
