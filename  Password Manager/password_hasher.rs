use std::env;
use ring::digest;

fn main() {
    // Get password from command line argument
    let args: Vec<String> = env::args().collect();
    let password = &args[1];

    // Hash the password using SHA-256
    let hashed_password = digest::digest(&digest::SHA256, password.as_bytes());

    // Print the hashed password as hexadecimal
    println!("{:x}", hashed_password);
}
