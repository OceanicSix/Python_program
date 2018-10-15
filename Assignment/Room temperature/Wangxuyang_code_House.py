import random
import copy

class house:
    def __init__(self, the_i_t = 20):
        self.i_t = the_i_t
        self.cost = 0

    def new_t(self, the_e_t):
        if the_e_t > self.i_t:
            #self.i_t = (self.i_t * 3 + the_e_t) / 4
            self.i_t = (self.i_t + the_e_t) / 2
        elif the_e_t < self.i_t:
            #self.i_t = (self.i_t * 7 + the_e_t) / 8
            self.i_t = (self.i_t * 3 + the_e_t) / 4
        return(self.i_t)

    def aconditioner(self, mode = 3):
        if mode == 1:
            self.cost += 49
            self.i_t -= 5
            return(self.i_t)
        elif mode == 2:
            self.cost += 12
            self.i_t -= 2
            return(self.i_t)
        elif mode == 3:
            return(self.i_t)
        elif mode == 4:
            self.cost += 5
            self.i_t += 1
            return(self.i_t)
        elif mode == 5:
            self.cost += 39
            self.i_t += 6
            return(self.i_t)

    def rt_delta(self, r):
        if self.i_t > (20 + r):
            return(self.i_t - 20 - r)
        elif self.i_t < (20 - r):
            return(20 - r - self.i_t)
        else:
            return(0)

class house_g:
    def __init__(self, the_e_t_list = [], the_ctr_list = []):
        self.my_house = house()
        self.e_t_list = the_e_t_list
        self.i_t_list = []
        self.ctr_list = the_ctr_list
        self.delta = 0

    def happy(self):
        for i in range(self.e_t_list.__len__()):
            self.my_house.new_t(self.e_t_list[i])
            j = self.my_house.aconditioner(self.ctr_list[i])
            if j > 22:
                self.delta += (j - 22)
            elif j < 18:
                self.delta += (18 - j)

    def rt_cost(self):
        return self.my_house.cost

    def rt_delta(self):
        return self.delta

class evolver:
    def __init__(self, the_t_list = [], the_population = 20):
        self.t_list = the_t_list
        self.population = the_population
        self.generation = []
        self.round_delta = 0
        self.round_cost = 0
        self.round_ctr_list = []
        self.f_m = 1000
        #self.generation_house = []
        for i in range(self.population):
            self.generation.append([])
            for j in range(self.t_list.__len__()):
                self.generation[i].append(random.randint(1,5))

    def mutation(self, fm_list):
        f_ctr_list = copy.copy(self.generation[fm_list[0]])
        m_ctr_list = copy.copy(self.generation[fm_list[1]])
        self.generation.clear()
        same_list = []
        for i in range(f_ctr_list.__len__()):
            if f_ctr_list[i] == m_ctr_list[i]:
                same_list.append(i)
        #print(f_ctr_list)
        #print(m_ctr_list)
        for i in range(self.population):
            self.generation.append([])
            for j in range(self.t_list.__len__()):
                if j in same_list:
                    self.generation[i].append(f_ctr_list[j])
                else:
                    self.generation[i].append(random.randint(1, 5))
        return(same_list.__len__())


    def processor(self):
        g_house_list = []
        for i in self.generation:
            g_house_list.append(house_g(self.t_list,i))
            g_house_list[-1].happy()
        return(g_house_list)

    def find_l_delta(self):
        g_house_list = self.processor()
        if g_house_list[0].rt_delta() < g_house_list[1].rt_delta():
            f_delta = g_house_list[0].rt_delta()
            m_delta = g_house_list[1].rt_delta()
            f = 0
            m = 1
        else:
            f_delta = g_house_list[1].rt_delta()
            m_delta = g_house_list[0].rt_delta()
            f = 1
            m = 0
        ii = 2
        for i in g_house_list[2:-1]:
            if i.rt_delta() < f_delta:
                f = ii
                f_delta = i.rt_delta()
            elif i.rt_delta() > f_delta and i.rt_delta() < m_delta:
                m = ii
                m_delta = i.rt_delta()
            ii += 1
        print("Delta = " + str(f_delta) + "  " + str(m_delta) + "  " + str(g_house_list[f].rt_cost()))
        self.round_delta = f_delta
        self.round_cost = g_house_list[f].rt_cost()
        self.round_ctr_list = copy.copy(self.generation[f])
        self.f_m = m_delta - f_delta
        return([f,m])

    # def find_l_cost(self):
    #     g_house_list = self.processor()
    #     if g_house_list[0].rt_delta() < g_house_list[1].rt_delta():
    #         f_delta = g_house_list[0].rt_delta()
    #         f = 0
    #     else:
    #         f_delta = g_house_list[1].rt_delta()
    #         f = 1
    #     ii = 2
    #     for i in g_house_list[2:-1]:
    #         if i.rt_delta() < f_delta:
    #             f = ii
    #             f_delta = i.rt_delta()
    #         ii += 1
    #     # m_cost start
    #     ii = 2
    #     if g_house_list[0].rt_cost() < g_house_list[1].rt_cost():
    #         m_cost = g_house_list[0].rt_cost()
    #         m = 0
    #     else:
    #         m_cost = g_house_list[1].rt_cost()
    #         m = 1
    #     for i in g_house_list[2:-1]:
    #         if i.rt_cost() < m_cost:
    #             m = ii
    #             m_cost = i.rt_cost()
    #         ii += 1
    #     print("Delta = " + str(f_delta) + "  " + "Cost = " + str(m_cost))
    #     return([f,m])


    def round(self, type = 'd', count = 200):
        if type == "d":
            j = 0
            for i in range(count):
                if self.mutation(self.find_l_delta()) == self.t_list.__len__():
                    break
                if self.f_m < 1:
                    j += 1
                elif self.f_m >= 1:
                    j = 0
                if j == 5:
                    break
                if self.population > 3000:
                    self.population = int(self.population / 1.5)
                print(self.population)
        elif type == "c":
            for i in range(count):
                self.mutation(self.find_l_cost())
        return([self.round_delta, self.round_ctr_list])


class simple1:
    def __init__(self, the_t_list=[]):
        self.e_t_list = the_t_list
        self.my_house = house()
        self.ctr_list = []
        self.delta = 0
        self.total_delta = 0
        self.cost = 0
        self.vio_count = 0

    def step(self, e_t):
        n_t = self.my_house.new_t(e_t)
        k = []
        k.append(n_t - 5)
        k.append(n_t - 2)
        k.append(n_t)
        k.append(n_t + 1)
        k.append(n_t + 6)
        delta = 100
        min_delta = 100
        min_index = 0
        ii = 0
        for i in k:
            if i > 22:
                delta = i - 22
            elif i < 18:
                delta = 18 - i
            else:
                delta = 0
            if delta < min_delta:
                min_delta = delta
                min_index = ii
            ii += 1
        self.delta = min_delta
        self.total_delta += min_delta
        min_index += 1
        self.my_house.aconditioner(min_index)
        return((min_index))

    def round(self):
        for i in self.e_t_list:
            self.ctr_list.append(self.step(float(i)))
            if self.ctr_list[-1] == 1:
                j = 'S'
            elif self.ctr_list[-1] == 2:
                j = 'C'
            elif self.ctr_list[-1] == 3:
                j = 'N'
            elif self.ctr_list[-1] == 4:
                j = 'H'
            elif self.ctr_list[-1] == 5:
                j = 'O'
            if self.delta == 0:
                k = "\t"
            else:
                k = "\t" + round(self.delta,1).__str__()
                self.vio_count += 1
            print(str(i) + "\t" + round(self.my_house.i_t).__str__() + "\t" + j + "\t" + self.my_house.cost.__str__() + "\t" + k + "\t" + self.vio_count.__str__() + "\t" + round(self.total_delta,1).__str__())




class simple2:
    def __init__(self, the_t_list=[], the_r = 2):
        self.e_t_list = the_t_list
        self.my_house = house()
        self.ctr_list = []
        self.delta = 0
        self.total_delta = 0
        self.cost = 0
        self.vio_count = 0
        self.r = the_r


    def step(self, e_t):
        n_t = self.my_house.new_t(e_t)
        k = []
        k.append(n_t)#3
        k.append(n_t + 1)#4
        k.append(n_t - 2)#2
        k.append(n_t + 6)#5
        k.append(n_t - 5)#1
        delta = 100
        min_delta = 100
        min_index = 0
        ii = 0
        for i in k:
            if i > (20 + self.r):
                delta = i - 20 - self.r
            elif i < (20 - self.r):
                delta = 20 - self.r - i
            else:
                delta = 0
            if delta < min_delta:
                min_delta = delta
                min_index = ii
            ii += 1
        self.delta = min_delta
        self.total_delta += min_delta
        if min_index == 0:
            min_index = 3
        elif min_index == 1:
            min_index = 4
        elif min_index == 2:
            min_index = 2
        elif min_index == 3:
            min_index = 5
        elif min_index == 4:
            min_index = 1
        self.my_house.aconditioner(min_index)
        return((min_index))

    def g_round(self):
        for i in self.e_t_list:
            self.ctr_list.append(self.step(float(i)))
            if self.ctr_list[-1] == 1:
                j = 'S'
            elif self.ctr_list[-1] == 2:
                j = 'C'
            elif self.ctr_list[-1] == 3:
                j = 'N'
            elif self.ctr_list[-1] == 4:
                j = 'H'
            elif self.ctr_list[-1] == 5:
                j = 'O'
            if self.delta == 0:
                k = "\t"
            else:
                k = "\t" + round(self.delta,1).__str__()
                self.vio_count += 1
            print(str(i) + "\t" + round(self.my_house.i_t).__str__() + "\t" + j + "\t" + self.my_house.cost.__str__() + "\t" + k + "\t" + self.vio_count.__str__() + "\t" + round(self.total_delta,1).__str__())

#------------------------------------------start from here--------------------------------
class simple7:
    def __init__(self, the_t_list=[], the_r = 2):
        self.e_t_list = the_t_list
        self.my_house = house()
        self.ctr_list = []
        self.delta = 0
        self.total_delta = 0
        self.cost = 0
        self.vio_count = 0
        self.r = the_r


    def step(self, e_t7 = []):
        best_k = []
        min_delta = 1000
        #min_cost = 10000
        for i1 in [3, 4, 2, 5, 1]:
            for i2 in [3, 4, 2, 5, 1]:
                for i3 in [3, 4, 2, 5, 1]:
                    for i4 in [3, 4, 2, 5, 1]:
                        for i5 in [3, 4, 2, 5, 1]:
                            for i6 in [3, 4, 2, 5, 1]:
                                for i7 in [3, 4, 2, 5, 1]:
                                    n_house = copy.copy(self.my_house)
                                    k = [i1, i2, i3, i4, i5, i6, i7]
                                    kk = 0
                                    delta = 0
                                    for j in e_t7:
                                        n_house.new_t(j)
                                        n_house.aconditioner(k[kk])
                                        delta += n_house.rt_delta(self.r)
                                        kk += 1
                                    if delta < min_delta:
                                        min_delta = delta
                                        best_k = k
                                    # elif delta == min_delta and n_house.cost < min_cost:
                                    #     min_cost = n_house.cost
                                    #     best_k = k
        self.delta = min_delta
        return(best_k)

    def g_round(self):
        for i in range(self.e_t_list.__len__()):
            if i < (self.e_t_list.__len__() - 7):
                self.ctr_list.append(self.step(self.e_t_list[i:i + 7])[0])
                self.my_house.new_t(self.e_t_list[i])
                self.my_house.aconditioner(self.ctr_list[-1])
                if self.ctr_list[-1] == 1:
                    j = 'S'
                elif self.ctr_list[-1] == 2:
                    j = 'C'
                elif self.ctr_list[-1] == 3:
                    j = 'N'
                elif self.ctr_list[-1] == 4:
                    j = 'H'
                elif self.ctr_list[-1] == 5:
                    j = 'O'
                if self.my_house.rt_delta(self.r) == 0:
                    k = "\t"
                else:
                    k = "\t" + round(self.my_house.rt_delta(self.r), 1).__str__()
                    self.vio_count += 1
                    self.total_delta += self.my_house.rt_delta(self.r)
                print(str(i) + "\t" + round(
                    self.my_house.i_t).__str__() + "\t" + j + "\t" + self.my_house.cost.__str__() + "\t" + k + "\t" + self.vio_count.__str__() + "\t" + round(
                    self.total_delta, 1).__str__())
            else:
                self.ctr_list += (self.step(self.e_t_list[i:i + 7]))
                for l in range(7):
                    self.my_house.new_t(self.e_t_list[i + l])
                    self.my_house.aconditioner(self.ctr_list[l - 7])
                    if self.ctr_list[l - 7] == 1:
                        j = 'S'
                    elif self.ctr_list[l - 7] == 2:
                        j = 'C'
                    elif self.ctr_list[l - 7] == 3:
                        j = 'N'
                    elif self.ctr_list[l - 7] == 4:
                        j = 'H'
                    elif self.ctr_list[l - 7] == 5:
                        j = 'O'
                    if self.my_house.rt_delta(self.r) == 0:
                        k = "\t"
                    else:
                        k = "\t" + round(self.my_house.rt_delta(self.r), 1).__str__()
                        self.vio_count += 1
                        self.total_delta += self.my_house.rt_delta(self.r)
                    print(str(i + l) + "\t" + round(
                        self.my_house.i_t).__str__() + "\t" + j + "\t" + self.my_house.cost.__str__() + "\t" + k + "\t" + self.vio_count.__str__() + "\t" + round(
                        self.total_delta, 1).__str__())
                break



def main():
    #filename = input("Pleas input the file name:")
    #filename = "JAN0107.txt"
    filename = "APR0814.txt"
    #filename = "AUG0107.txt"
    #filename = "OCT0107.txt"
    r = 2
    wfilename = "text.txt"
    et_file = open(filename, "r")
    e_t_list = []
    j = et_file.readline()
    while (j != ''):
        e_t_list.append(float(j))
        j = et_file.readline()
    et_file.close()

    new_simple = simple7(e_t_list,r)
    new_simple.g_round()
    print(str(new_simple.total_delta))
    # new_simple = simple1(e_t_list)
    # new_simple.g_round()
    # print(str(new_simple.delta))


    # while(True):
    #     new_evolver = evolver(e_t_list,16000)
    #     new_evolver.round('d',50)
    #     print(new_evolver.round_ctr_list.__str__() + "  " + new_evolver.round_delta.__str__() + "  " + new_evolver.round_cost.__str__())
    #     result_file = open(wfilename, "a")
    #     result_file.write('\n' + new_evolver.round_ctr_list.__str__() + "  " + new_evolver.round_delta.__str__() + "  " + new_evolver.round_cost.__str__())
    #     result_file.close()

    #print(str(new_evolver.round_delta) + new_evolver.round_ctr_list)
    # new_house = house()
    # for i in e_t_list:
    #     new_house.new_t(i)
    # print(round(new_house.i_t,1))


if __name__ == "__main__":
    main()