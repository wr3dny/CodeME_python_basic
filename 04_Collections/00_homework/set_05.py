# 5 Porównaj zachowanie discard() vs remove() dla typu set.

created_set = {'warszawa', 'sopot', 'chorzów'}

created_set.discard('opole') # nic nie usunie, nie wypluje błędu
created_set.remove('opole') # nic nie usunie, ale wyrzucić error