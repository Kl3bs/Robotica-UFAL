import setup as main


A_1 = main.transl(-1, 0, 0) @ main.trotz(main.np.pi/2)
A_2 = main.transl(0, 0, 0) @ main.trotz(main.np.pi/2) @ main.trotx(main.np.pi/2)
A_3 = main.transl(2, 0, 0) @ main.trotz(main.np.pi/2) @ main.trotx(main.np.pi/2) @ main.trotx(-main.np.pi/2) 
 

main.trplot(A_1, frame="A", color="green")
main.trplot(A_2, frame="A2", color="b")
main.trplot(A_2, frame="A3", color="purple")
 
main.plt.show()