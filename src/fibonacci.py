from nada_dsl import *


def get_new_fib(f1,f2):
    return f1 + f2


def get_fib(max_iter,f_num,party_alice):
    f1 = Integer(0)
    f2 = Integer(0)
    nfib = Integer(0)
    for i in range(max_iter):
        if i == 1:
            f1 = Integer(1)
        cond1 = f_num > Integer(0)
        nfib = cond1.if_else(get_new_fib(f1, f2), nfib)
        f_num = f_num - Integer(1)
        f2 = f1
        f1 = nfib
    return nfib

def nada_main():
      party_alice = Party(name="Alice")

      max_iter = 100
      f_num = SecretInteger(Input(name="f_num", party=party_alice))

      is_max_cond = f_num < Integer(max_iter)
      nfib = is_max_cond.if_else(get_fib(max_iter,f_num, party_alice), Integer(4))

      out = Output(nfib, "res_fib", party_alice)

      return [out]
