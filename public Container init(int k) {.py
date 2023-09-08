public Container init(int k) {
		Container cn = this.getContentPane();
		pn = new JPanel();
		pn.setLayout(new GridLayout(m,n));
		for (int i = 0; i < m; i++)
			for (int j = 0; j < n; j++){
				bt[i][j] = new JButton();
				pn.add(bt[i][j]);
				bt[i][j].setActionCommand(i + " " + j);
				bt[i][j].addActionListener(this);
				bt[i][j].addKeyListener(this);
				bt[i][j].setBorder(null);
				a[i][j] = 0;
			}
		
		pn2 = new JPanel();
		pn2.setLayout(new FlowLayout());
		
		newGame_bt = new JButton("New Game");
		newGame_bt.addActionListener(this);
		newGame_bt.addKeyListener(this);
		newGame_bt.setFont(new Font("UTM Micra", 1, 15));
		newGame_bt.setBackground(Color.white);
		
		score_bt = new JButton("3");
		score_bt.addActionListener(this);
		score_bt.addKeyListener(this);
		score_bt.setFont(new Font("UTM Micra", 1, 15));
		score_bt.setBackground(Color.white);
		
		for (int i = 1; i <= speed.length; i++)
			lv.addItem("Mức độ " + i);
		lv.setSelectedIndex(k);
		lv.addKeyListener(this);
		lv.setFont(new Font("UTM Micra", 1, 15));
		lv.setBackground(Color.white);
		
		pn2.add(newGame_bt);
		pn2.add(lv);
		pn2.add(score_bt);
		
		a[m / 2][n / 2 - 1] = 1;
		a[m / 2][n / 2] = 1;
		a[m / 2][n / 2 + 1] = 2;
		xSnake[0] = m / 2;
		ySnake[0] = n / 2 - 1;
		xSnake[1] = m / 2;
		ySnake[1] = n / 2;
		xSnake[2] = m / 2;
		ySnake[2] = n / 2 + 1;
		sizeSnake = 3;
		
		creatFood();
		updateColor();
		cn.add(pn);
		cn.add(pn2, "South");
		this.setVisible(true);
		this.setSize(n * 30, m * 30);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setLocationRelativeTo(null);
		return cn;
	longphan