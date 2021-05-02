""""""
import matplotlib.pyplot as plt
import cmath
import math
import argparse
import logging


def first():
    plt.grid()
    for im in range(0,10):
        xs = [0]
        ys = [0]
        s = 1.1+im*1j
        summe = 0
        for n in range(1,1000):
            real_power = math.pow(n, -s.real)
            imag_power = cmath.exp(-1j*s.imag*math.log(n))
            res = real_power * imag_power
            summe += res
            xs.append(res.real+xs[-1])
            ys.append(res.imag+ys[-1])
        ax = plt.plot(xs, ys, '-o', label=str(s))
        print(s, summe, abs(summe))
    plt.legend()
    plt.show()


def complex_power(j, s):
    real_power = math.pow(j, s.real)
    imag_power = cmath.exp(-1j*s.imag*math.log(j))
    res = real_power * imag_power
    return res


def B(k):
    Bernoulli = [1.0, -1.0/2.0, 1.0/6.0, 0.0, -1.0/30.0, 0.0,
                 1.0/42.0, 0.0, -1.0/30.0, 0.0, 5.0/66.0, 0.0, -691.0/2730.0,
                 0.0, 7.0/6.0, 0.0, -3617.0/510.0, 0.0, 43867.0/798.0, 0.0, -174611.0/330.0]
    numerator = [1, -1, 1, 0, -1, 0, 1, 0, -1, 0, 5, 0, -691, 0, 7, 0, -3617, 0, 43867, 0, -174611, 0, 854513, 0, -236364091, 0, 8553103, 0, -23749461029, 0, 8615841276005, 0, -7709321041217, 0, 2577687858367, 0, -26315271553053477373, 0, 2929993913841559, 0, -261082718496449122051]
    denominator = [1, 2, 6, 1, 30, 1, 42, 1, 30, 1, 66, 1, 2730, 1, 6, 1, 510, 1, 798, 1, 330, 1, 138, 1, 2730, 1, 6, 1, 870, 1, 14322, 1, 510, 1, 6, 1, 1919190, 1, 6, 1, 13530, 1, 1806, 1, 690, 1, 282, 1, 46410, 1, 66, 1, 1590, 1, 798, 1, 870, 1, 354, 1, 56786730, 1]
    return numerator[k]/denominator[k]


def T(k, n, s):
    product = 1
    for j in range(2*k-2+1):
        product *= s+j
    return B(2*k)/math.factorial(2*k)*complex_power(n, 1-s-2*k) * product


def second(s):
    n = 20
    m = 20

    neg_s = -1.0 * s

    part1 = 0
    for j in range(1, n):
        part1 += complex_power(j, neg_s)

    #print(part1)

    part2 = 0.5 * complex_power(n, neg_s)

    #print(part2)

    part3 = complex_power(n, 1-s) / (s-1)

    #print(part3)

    part4 = 0
    for k in range(1, m+1):
        part4 += T(k, n, s)

    #print(part4)

    print("{} -> {}".format(s, part1+part2+part3+part4))


def main():
    # create logger
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

    description_string = 'Do something.'
    parser = argparse.ArgumentParser(description=description_string)
    parser.add_argument('someparam', type=str, help='some param')
    parser.add_argument('--foo', type=int, help='some int', required=True)

    args = parser.parse_args()


if __name__ == "__main__":
    known_values = {0.0: -0.5,
                    0.5+14.1347251417j: 0.0,
                    0.5+21.0220396387j: 0.0,
                    0.5+25.0108575801j: 0.0,
                    -1.0: -1.0/12.0,
                    -3.0: -1.0/120.0,
                    2.0: math.pi*math.pi/6.0,
                    3.0: 1.2020569}
    for k, v in known_values.items():
        print("Evaluated:")
        second(k)
        print("Known:")
        print("{} -> {}".format(k, v))
