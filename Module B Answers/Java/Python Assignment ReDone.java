package me.kiran.pythonassignment;

import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

public class Core {

	private Scanner scanner;

	public Core() {

		scanner = new Scanner(System.in);

		while (true) {
			System.out.println("Please enter project #");
			System.out.println("1 - 5");

			int projectNumber = scanner.nextInt();

			switch (projectNumber) {
			case 1:
				System.out.println("Running Program #1");
				int numVal = 6;
				numVal -= 1;
				System.out.println("Result for Program #1: " + numVal);
				break;
			case 2:
				System.out.println("Running Program #2");
				System.out.print("Please enter some text: ");
				String userInput = scanner.next();
				System.out.println("The string you typed was: " + userInput);
				break;
			case 3:
				System.out.println("Running Program #3");
				System.out.print("Please enter a number: ");
				numVal = 0;
				numVal = scanner.nextInt();
				if (numVal > 5) {
					System.out.println("Your number is greater than 5");
				} else if (numVal < 5) {
					System.out.println("Your number is less than 5");
				}
				break;
			case 4:
				System.out.println("Running Program #4");
				System.out.print("Please enter a number for countdown: ");
				int countdown = scanner.nextInt();
				while (countdown != -1) {
					System.out.println("Countdown: " + countdown);
					countdown -= 1;
					if (countdown == -1) {
						System.out.println("Blastoff!!!");
					}
				}
				break;
			case 5:
				int computerNumber = ThreadLocalRandom.current().nextInt(1, 9 + 1);
				boolean guessedRight = false;
				while (!guessedRight) {
					System.out.print("Please guess a number between (1-10): ");
					int userGuess = scanner.nextInt();
					if (computerNumber == userGuess) {
						System.out.println("You guesed the correct number!");
						guessedRight = true;
					} else if (computerNumber < userGuess) {
						System.out.println("That number is too high!");
					} else if (computerNumber > userGuess) {
						System.out.println("That number is too low!");
					}
				}
				break;
			default:
				break;
			}
		}
	}

	public static void main(String[] args) {
		new Core();
	}
}
