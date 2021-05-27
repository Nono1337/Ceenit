import { Component, OnInit } from '@angular/core';
import { HttpServiceService } from 'src/app/service/http-service.service';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-movie-detail',
  templateUrl: './movie-detail.component.html',
  styleUrls: ['./movie-detail.component.css'],
})
export class MovieDetailComponent implements OnInit {
  movie;
  constructor(
    private httpServe: HttpServiceService,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.httpServe
      .getMovieDetailsById(this.route.snapshot.paramMap.get('id'))
      .subscribe((resp) => {
        console.log(resp);
        if (resp != undefined) {
          // @ts-ignore: TS2339
          this.movie = resp;
          this.movie.link = "https://image.tmdb.org/t/p/w500/"
        }
      });
  }
}
