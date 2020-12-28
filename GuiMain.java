package guidemo;

import javax.swing.SwingUtilities;

public class GuiMain {

	public static void main(String[] args) {
		SwingUtilities.invokeLater(new Runnable() {
			/*
			 * because file btn was not working i.e we set its priority first
			 */
			@Override
			public void run() {
				new TicTacToeGui();
				
			}
		});
		
	}

}
