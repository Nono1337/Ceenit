import { Component, OnInit} from '@angular/core';
import { MatSidenavModule } from '@angular/material/sidenav';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  title = 'ceenit';
  opened = false;
  constructor(private router: Router) {}
  ngOnInit() {}

  searchHandler(searchInput) {
    console.log("Die Suche lautet: "+ searchInput.value);
    this.router.navigateByUrl('/search/' + searchInput.value);
  }
  userMenu() {}
}
