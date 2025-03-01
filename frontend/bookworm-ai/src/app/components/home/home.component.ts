import { Component } from '@angular/core';
import { NavbarComponent } from '../navbar/navbar.component';
import { FormsModule } from '@angular/forms';
import { NgIf } from '@angular/common';

@Component({
  selector: 'app-home',
  imports: [NgIf, FormsModule, NavbarComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  name: string = '';
  nameColor: string = 'red';
  placeholderText: string = 'Enter your name';
  switch: boolean = false

  changeName(name: string) {
    this.name = name;
    console.log(this.name);
  }

  onClick() {
    if(this.switch) this.switch = false;
    else this.switch = true;
  }
}
