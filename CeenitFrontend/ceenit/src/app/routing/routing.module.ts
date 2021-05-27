import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { CeenitListsComponent } from '../ceenit-lists/ceenit-lists.component';
import { CeenitReviewsComponent } from '../ceenit-reviews/ceenit-reviews.component';
import { CeenitTimelineComponent } from '../ceenit-timeline/ceenit-timeline.component';
import { CeenitWatchlistComponent } from '../ceenit-watchlist/ceenit-watchlist.component';
import { HomeComponent } from '../home/home.component';
import { SearchComponent } from '../search/search.component';
import { MovieDetailComponent } from '../movie-detail/movie-detail.component';
HomeComponent
CeenitWatchlistComponent
CeenitTimelineComponent
CeenitReviewsComponent
CeenitListsComponent

const routes: Routes = [
  { path: 'lists', component: CeenitListsComponent},
  { path: 'reviews', component: CeenitReviewsComponent},
  { path: 'timeline', component: CeenitTimelineComponent},
  { path: 'watchlist', component: CeenitWatchlistComponent},
  { path: 'home', component: HomeComponent },
  { path: 'detail', component: MovieDetailComponent},
  { path: 'search/:title', component: SearchComponent },
  { path: 'movie/:id', component: MovieDetailComponent},
  { path: '', redirectTo: '/home', pathMatch: 'full'}

]



@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ]
})
export class RoutingModule { }
