import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-navbar',
  imports: [FormsModule, RouterOutlet, RouterLink],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {
  searchTerm: string = '';
  genre: string = 'Select a genre';

  // Create a function to redirect to about page
  aboutPage() {
    window.location.href = '/about';
  }
}
