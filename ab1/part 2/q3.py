from tabulate import tabulate


table = [['i', 'αi-1', 'ai-1', 'θi'], 
         ['1', 'L1', '0', 'θ1'], 
         ['2', 'L2', '0', 'θ2'], 
         ['3', '0', '0', 'θ3'],
         ['4', '0', '0', 'θ4']]

print(tabulate(table))
