import { MovieList } from './../../Model/movie.model';
import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-movie-list',
  templateUrl: './movie-list.component.html',
  styleUrls: ['./movie-list.component.css']
})
export class MovieListComponent implements OnInit {
  @Input() lstMovies : MovieList[];
  constructor() { }

  ngOnInit(): void {
  }

}
