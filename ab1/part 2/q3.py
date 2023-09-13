from tabulate import tabulate


table = [['i', 'αi-1', 'ai-1', 'di' ,'θi'], 
         ['1', '0', 'L1','d1c' , 'θ1'], 
         ['2', '0', 'L2','0' , 'θ2'], 
         ['3', '0', '0', '0' ,'θ3'],
         ['4', 'π', '0', 'd3' ,'θ4']]

print(tabulate(table))
