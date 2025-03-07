import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { NgFor, NgIf } from '@angular/common';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-home',
  imports: [NgIf, NgFor, FormsModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  name: String = '';
  nameColor: String = 'red';
  placeholderText: String = 'Enter your name';
  switch: boolean = false;
  bookList: String[] = ["The Hunger Games", "And Then There Were None", "Atomic Habits"];
  bookName: String = '';

  constructor(private http: HttpClient) {
    this.http.get("http://127.0.0.1:5000/books").subscribe((result: any) => {
      this.bookList = result;
    });
  }

  changeName(name: string) {
    this.name = name;
    console.log(this.name);
  }

  onClick() {
    if(this.switch) this.switch = false;
    else this.switch = true;
  }

  add() {
    if(this.bookName != "") this.bookList.push(this.bookName);
    this.bookName = '';
  }

  remove(book: String) {
    this.bookList = this.bookList.filter(b => b !== book);
  }
}
