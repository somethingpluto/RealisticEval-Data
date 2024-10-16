import java.io.*;
import java.net.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Solutions to problem 1 of cs10 final practice exam
 * Handles communication between the server and one client, for ChatServer
 *
 * @author warrenshepard, Spring 2023
 * @author Chris Bailey-Kellogg, Dartmouth CS 10, Fall 2012; revised Spring 2014 to separate out ChatServerFromClient
 */
public class ChatServerCommunicator extends Thread {
	private Socket sock;					// each instance is in a different thread and has its own socket
	private ChatServer server;				// the main server instance
	private String name;					// client's name (first interaction with server)
	private BufferedReader in;				// from client
	private PrintWriter out;				// to client
	private boolean access = false;			// if client has access to the server
	private boolean connected = true;

	public ChatServerCommunicator(Socket sock, ChatServer server) {
		this.sock = sock;
		this.server = server;
	}
	public void kick() throws IOException {
		server.removeCommunicator(this);
		server.broadcast(this, name + " has been kicked off the server!");
		out.println("you've been kicked out");
		connected = false;
	}

	public void run() {
		try {
			System.out.println("someone connected");

			// Communication channel
			in = new BufferedReader(new InputStreamReader(sock.getInputStream()));
			out = new PrintWriter(sock.getOutputStream(), true);

			// Identify -- first message is the name
			name = in.readLine();
			System.out.println("it's " + name);
			out.println("welcome " + name);
			server.clients.put(name, this);
			server.broadcast(this, name + " entered the room");


			// Chat away
			String line;
			while ((line = in.readLine()) != null && connected) {
				String[] message = line.split(": ");
				String command = message[0];

				if (command.equals("RENAME") && message.length > 1) {
					String newName = message[1];
					server.clients.remove(name);
					server.clients.put(name, this);
					name = newName;
				}
				else if (command.equals("KICK") && message.length > 1) {
					if (access) {
						String name = message[1];
						if (server.clients.containsKey(name)) {
							ChatServerCommunicator serverComm = server.clients.get(name);
							System.out.println("yo");
							server.clients.remove(name);
							serverComm.kick();
						}
						else {
							out.println("ERROR: The specified client does not exist");
						}
					} else {
						out.println("ERROR: you do not have permission to kick clients out.");
					}

				}
				else if (command.equals("PASSWORD") && message.length > 1) {
					String password = message[1];
					if (server.isPassword(password)) {
						out.println("correct password");
						access = true;
					} else {
						out.println("incorrect password");
					}
				}
				else if (command.equals("PRIVATE MESSAGE") && message.length > 1) {
					String name = message[1];
					if (server.clients.containsKey(name)) {
						ChatServerCommunicator serverComm = server.clients.get(name);
						String pm = "Private message from " + this.name + ": " + message[2];
						serverComm.send(pm);
					}
					else {
						out.println("ERROR: The specified client does not exist");
					}

				}
				else if (command.equals("ADD EMAIL") && message.length > 1) {
					String email = message[1];
					out.println(email);

					String emailRegex = "^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$";		//advanced regex for email, generated by chatGPT (yours does not need to be as complex)
					Pattern pattern = Pattern.compile(emailRegex);
					Matcher matcher = pattern.matcher(email);
					boolean matchFound = matcher.matches();

					if (matchFound) {
						server.emails.put(name, email);
						out.println("Email added successfully!");
					}
					else {
						out.println("Email is in incorrect format. Please add email in the correct format.");
					}


				}
				else if (command.equals("GET EMAIL") && message.length > 1) {
					String name = message[1];
					if (server.emails.containsKey(name)) {
						String email = server.emails.get(name);
						out.println(name + "'s email: " + email);
					}
					else {
						out.println("ERROR: The specified client either does not exist or has not uploaded their email");
					}

				} else {
					server.broadcast(this, name +": " + line);
				}
			}

			// Done
			System.out.println(name + " hung up");
			server.broadcast(this, name + " left the room");

			// Clean up -- note that also remove self from server's list of handlers so it doesn't broadcast here
			server.removeCommunicator(this);
			out.close();
			in.close();
			sock.close();
		}
		catch (IOException e) {
			e.printStackTrace();
		}
	}

	/**
	 * Sends a message to the client
	 * @param msg
	 */
	public void send(String msg) {
		out.println(msg);
	}
}