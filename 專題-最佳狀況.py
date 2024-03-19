
import random
import numpy as np

z = int(input('跑幾次：'))
best = 0
averagebest = 0

for x in range(z):

    oil = 40
    crop = 40
    stock = 40
    bfi = 40
    gold = 40
    special = [1,2,3,4,5,6,7,8,9,10]
    normal = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
              21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,
              38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,
              55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,
              72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]

    for i in range(8):

        cropone = crop
        oilone = oil
        stockone = stock
        bfione = bfi
        goldone = gold
        
        tech = random.randint(1,5)
        b = random.choice(special)
        special.remove(b)
        
        if b == 1:
            up = [15,10,5,3,-3,-10]
            move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
            crop += move
            gold += move
        elif b == 2:
            upup = [15,10,5,3,-3,-10]         
            move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
            crop += move
            oil += move
        elif b == 3:
            up = [15,10,5,3,-3,-10]
            move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
            stock += move
            bfi += move
        elif b == 4:
            upup = [15,10,5,3,-3,-10]         
            move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
            stock += move
            bfi += move
        elif b == 5:
            up = [15,10,5,3,-3,-10]
            move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
            gold += move
            oil += move
        elif b == 6:
            downdown = [10,3,-3,-5,-15]
            move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
            stock += move
            gold += move
        elif b == 7:
            down = [5,3,-3,-5,-10]
            move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
            stock += move
            bfi += move
        elif b == 8:
            down = [5,3,-3,-5,-10]
            move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
            crop += move
            oil += move
        elif b == 9:
            down = [5,3,-3,-5,-10]
            move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
            gold += move
            bfi += move
        else:
            down = [5,3,-3,-5,-10]
            move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
            oil += move
            crop += move

        for y in range(4):

            c = random.choice(normal)
            normal.remove(c)

            if c == 1:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                stock += move
            elif c == 2:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                bfi += move
            elif c == 3:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                bfi += move
            elif c == 4:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                crop += move
            elif c == 5:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                oil += move
            elif c == 6:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                gold += move
            elif c == 7:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                crop += move
            elif c == 8:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                oil += move
            elif c == 9:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                oil += move
            elif c == 10:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                crop += move
            elif c == 11:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                gold += move
            elif c == 12:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                gold += move
            elif c == 13:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                stock += move
            elif c == 14:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                stock += move
            elif c == 15:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                bfi += move
            elif c == 16:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                stock += move
            elif c == 17:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                oil += move
            elif c == 18:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                crop += move
            elif c == 19:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                bfi += move
            elif c == 20:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                gold += move
            elif c == 21:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                crop += move
            elif c == 22:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                oil += move
            elif c == 23:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                oil += move
            elif c == 24:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                crop += move
            elif c == 25:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                gold += move
            elif c == 26:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                gold += move
            elif c == 27:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                bfi += move
            elif c == 28:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                stock += move
            elif c == 29:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                stock += move
            elif c == 30:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                bfi += move
            elif c == 31:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                crop += move
            elif c == 32:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                crop += move
            elif c == 33:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                stock += move
            elif c == 34:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                oil += move
            elif c == 35:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                oil += move
            elif c == 36:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                oil += move
            elif c == 37:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                bfi += move
            elif c == 38:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                gold += move
            elif c == 39:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                crop += move
            elif c == 40:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                stock += move
            elif c == 41:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                stock += move
            elif c == 42:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                bfi += move
            elif c == 43:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                bfi += move
            elif c == 44:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                gold += move
            elif c == 45:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                crop += move
            elif c == 46:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                oil += move
            elif c == 47:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                stock += move
            elif c == 48:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                gold += move
            elif c == 49:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                bfi += move
            elif c == 50:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                gold += move
            elif c == 51:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                crop += move
            elif c == 52:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                crop += move
            elif c == 53:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                stock += move
            elif c == 54:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                bfi += move
            elif c == 55:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                stock += move
            elif c == 56:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                oil += move
            elif c == 57:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                oil += move
            elif c == 58:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                bfi += move
            elif c == 59:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                gold += move
            elif c == 60:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                gold += move
            elif c == 61:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 62:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 63:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 64:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 65:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 66:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 67:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 68:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 69:
                upup = [15,10,5,3,-3,-10]
                move = int(np.random.choice(upup, 1, p = [0.0465,0.1157,0.2129,0.3657,0.2407,0.0185]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 70:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 71:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 72:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 73:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 74:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 75:
                up = [15,10,5,3,-3,-10]
                move = int(np.random.choice(up, 1, p=[0.0046,0.0417,0.1157,0.5788,0.2546,0.0046]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 76:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 77:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 78:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 79:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 80:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 81:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 82:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 83:
                downdown = [10,3,-3,-5,-15]
                move = int(np.random.choice(downdown, 1, p=[0.0185,0.2407,0.3659,0.2823,0.0926]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 84:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 85:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 86:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 87:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 88:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            elif c == 89:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move
            else:
                down = [5,3,-3,-5,-10]
                move = int(np.random.choice(down, 1, p=[0.0046,0.2546,0.4816,0.2407,0.0185]))
                if tech == 1: oil += move
                elif tech == 2: crop += move
                elif tech == 3: stock += move
                elif tech == 4: bfi += move
                else: gold += move

        croptwo = crop
        oiltwo = oil
        stocktwo = stock
        bfitwo = bfi
        goldtwo = gold

        cropthree = croptwo - cropone
        oilthree = oiltwo - oilone
        stockthree = stocktwo - stockone
        bfithree = bfitwo - bfione
        goldthree = goldtwo - goldone

        compare = []
        compare.append(cropthree)
        compare.append(oilthree)
        compare.append(stockthree)
        compare.append(goldthree)
        compare.append(bfithree)
        compare.sort(reverse = True)
        best += compare[0]
        
        
    
averagebest = best/(8*z)
print('最佳狀況的每回合平均上漲金額', averagebest)
