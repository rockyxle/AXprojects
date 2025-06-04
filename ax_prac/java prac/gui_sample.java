import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class gui_sample implements ActionListener {

    private int count = 0;
    private JLabel label;
    private JFrame frame;
   
    private JPanel panel;

    public gui_sample() {
         frame = new JFrame();


        JButton button = new JButton("Click me");
        button.addActionListener(this);
        label = new JLabel("Number of Clicks: 0");


        panel = new JPanel();
        panel.setBorder(BorderFactory.createEmptyBorder(30, 30, 10, 30));
        panel.setLayout(new GridLayout(0,1));
        panel.setAlignmentY(500);
        panel.setBackground(java.awt.Color.RED);
        panel.setAlignmentX(500);
        
        panel.add(button); // Add the button to the panel
        panel.add(label);  // Add the label to the panel

        frame.add(panel, BorderLayout.CENTER);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("testing ng GUI hahahaha");
        frame.pack();
        frame.setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        count++;
        label.setText(("Number of clicks:  "+ count));
    }
    public static void main(String[] args) {
        new gui_sample();
    }
}