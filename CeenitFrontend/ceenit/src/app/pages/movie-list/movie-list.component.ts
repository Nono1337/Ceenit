import { SearchedMovie } from './../../Model/SearchedMovie.model';
import { Component, Input, OnInit } from '@angular/core';
import { Variable } from '@angular/compiler/src/render3/r3_ast';

@Component({
  selector: 'app-movie-list',
  templateUrl: './movie-list.component.html',
  styleUrls: ['./movie-list.component.css']
})
export class MovieListComponent implements OnInit {
  @Input() lstMovies : SearchedMovie[];
  constructor() { }

  ngOnInit(): void {
  }

  show(): void {
    console.log(this.lstMovies[0].movieId)
  }

  toggle(event): void {
    if (event.target.id == '')
    console.log(event.target.__ngContext__[0].id)
    else
    console.log(event.target.id)
  }
}
