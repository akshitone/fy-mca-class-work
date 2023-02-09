interface BankApp {
    number: number;
    holderName: string;
    type?: string;
    balance: number;
    withdraw(): void;
    deposit(): void;
    displayDetais(): void;
}

class Bank implements BankApp {
    number: number;
    holderName: string;
    balance: number;

    constructor(number: number, holderName: string, balance: number) {
        this.number = number;
        this.holderName = holderName;
        this.balance = balance;
    }

    withdraw(): void {
        throw new Error("Method not implemented.");
    }
    deposit(): void {
        throw new Error("Method not implemented.");
    }
    displayDetais(): void {
        throw new Error("Method not implemented.");
    }

}