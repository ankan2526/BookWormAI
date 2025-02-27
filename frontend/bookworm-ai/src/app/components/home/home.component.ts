import { Component } from '@angular/core';
import { NavbarComponent } from '../navbar/navbar.component';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-home',
  imports: [FormsModule, NavbarComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  name: string = '';
  nameColor: string = 'red';
  placeholderText: string = 'Enter your name';

  changeName(name: string) {
    this.name = name;
    console.log(this.name);
  }
}
