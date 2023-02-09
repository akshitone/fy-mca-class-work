class Account {
    number: number;
    holderName: string;
    type: string;
    balance: number;

    constructor(number: number, holderName: string, type: string, balance: number) {
        this.number = number;
        this.holderName = holderName;
        this.type = type;
        this.balance = balance;
    }

    withdraw(amount: number) {
        this.balance = this.balance - amount;
        console.log(`Current balance: ${this.balance}`);

    }

    deposit(amount: number) {
        this.balance = this.balance + amount;
        console.log(`Current balance: ${this.balance}`);

    }

    displayDetails(): void {
        console.log(`Account number: ${this.number}`);
        console.log(`Account holder name: ${this.holderName}`);
        console.log(`Account type: ${this.type}`);
        console.log(`Current balance: ${this.balance}`);

    }
}

const johnDoeAccount = new Account(123, 'John Doe', 'Savings', 2000);
johnDoeAccount.displayDetails();