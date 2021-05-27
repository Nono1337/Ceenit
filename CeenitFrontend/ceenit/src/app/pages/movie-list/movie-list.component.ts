import { SearchedMovie } from './../../Model/SearchedMovie.model';
import { Component, Input, OnInit } from '@angular/core';
import { Variable } from '@angular/compiler/src/render3/r3_ast';
import { Router } from '@angular/router';

@Component({
  selector: 'app-movie-list',
  templateUrl: './movie-list.component.html',
  styleUrls: ['./movie-list.component.css']
})
export class MovieListComponent implements OnInit {
  @Input() lstMovies : SearchedMovie[];
  constructor(private router: Router) {}

  ngOnInit(): void {
  }

  show(): void {
    console.log(this.lstMovies[0].movieId)
  }

  toggle(event): void {
    if (event.target.id == ''){
      this.router.navigateByUrl('/movie/' + event.target.__ngContext__[0].id);      
    }
    else {
      this.router.navigateByUrl('/movie/' + event.target.id);
    }
  }
}
