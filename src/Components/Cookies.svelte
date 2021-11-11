<script>
  import { onMount } from "svelte";
  import ExerciseItem from "./ExerciseItem.svelte";
  import { fade, fly } from "svelte/transition";

  export let AppObjects;
  export let saved_cookies = [];

  let ExerciseList = [];
  let ExerciseIndexList = [];

  let TemplateList = [];

  let Func = () => {};

  onMount(() => {
    let cookie_db = "saved_workouts";
    let cookie_db_value = "";

    if (
      !document.cookie // If db does not exist
        .split(";")
        .some((item) => item.trim().startsWith(cookie_db + "="))
    ) {
      return;
    } else {
      // Get db
      cookie_db_value = document.cookie
        .split("; ")
        .find((item) => item.startsWith(cookie_db + "="))
        .split("=")[1];
      let cookie_db_array = cookie_db_value.split(",");

      for (let id = 0; id < cookie_db_array.length; id++) {
        saved_cookies.push(cookie_db_array[id]);
      }
    }
    saved_cookies = saved_cookies;
  });

  function DeleteExercise(i) {
    let cookie_db = "saved_workouts";
    let cookie_db_value = "";

    let new_cookie_db_value;

    saved_cookies = [];

    if (
      !document.cookie // If db does not exist
        .split(";")
        .some((item) => item.trim().startsWith(cookie_db + "="))
    ) {
      return;
    } else {
      // Get db
      cookie_db_value = document.cookie
        .split("; ")
        .find((item) => item.startsWith(cookie_db + "="))
        .split("=")[1];
      let cookie_db_array = cookie_db_value.split(",");

      new_cookie_db_value = "";
      for (let id = 0; id < cookie_db_array.length; id++) {
        if (cookie_db_array[id] != i) {
          saved_cookies.push(cookie_db_array[id]);
          new_cookie_db_value = new_cookie_db_value + cookie_db_array[id] + ",";
        }
      }

      new_cookie_db_value =
        new_cookie_db_value.length > 0
          ? new_cookie_db_value.substr(0, new_cookie_db_value.length - 1) +
            "; SameSite=Lax;"
          : "; Max-Age=0; SameSite=Lax;";

      let new_cookie = cookie_db + "=" + new_cookie_db_value;
      document.cookie = new_cookie;
    }

    document.cookie = "workout_" + i + "=; Max-Age=0; SameSite=Lax;";
    saved_cookies = saved_cookies;
  }
  function LoadExerciseList(i) {
    ExerciseIndexList = [];
    ExerciseList = [];

    let cookie_name = "workout_" + i;
    const cookie_value = document.cookie
      .split("; ")
      .find((row) => row.startsWith(cookie_name + "="))
      .split("=")[1];
    let exercises = cookie_value.split(",");
    for (let i = 0; i < exercises.length; i++) {
      let exercise_id = exercises[i];
      ExerciseIndexList.push(exercise_id);

      let exercise = AppObjects.workoutObject[exercise_id];
      ExerciseList.push(exercise);
    }
  }

  let cookie_mode = -1;
</script>

<div class="scrollSpecial">
  {#if saved_cookies.length == 0}
    <h6 class="display-7">You have no saved workouts.</h6>
  {/if}

  <div class="row">
    <div class="col">
      <ul class="list-group list-group-flush">
        {#each saved_cookies as cookie, i}
          <li class="list-group-item bg-transparent liSpecial">
            <button
              class="btn btn-outline-secondary col text-secondary"
              on:click={() => {
                LoadExerciseList(cookie);
                cookie_mode = cookie_mode == i ? -1 : i;
              }}>Save {i}</button
            >
            <button
              class="btn bi bi-trash btn-outline-danger"
              style="font-size: 100%"
              on:click={() => {
                Func = () => {
                  DeleteExercise(cookie);
                };
                let myModal = new bootstrap.Modal(
                  document.getElementById("deleteModal")
                );
                myModal.toggle();
              }}
            />
          </li>
        {/each}
      </ul>
    </div>
  </div>

  {#if cookie_mode != -1}
    <div class="row" out:fade={{ duration: 400 }} in:fade={{ duration: 200 }}>
      <div class="col">
        <p
          class="btn-outline-secondary disabled"
          data-bs-toggle="tooltip"
          data-bs-placement="top"
          title="For each exercise you wish to add to your workout, you can filter out muscle group, difficulty, required equipment and exercise type."
        >
          Your results:
        </p>
        <ul class="list-group list-group-flush">
          {#each ExerciseList as exercise, i}
            <li class="list-group-item bg-transparent liSpecial">
              <ExerciseItem
                ExerciseEntry={exercise}
                ExerciseIndex={ExerciseIndexList[i]}
                id={i}
                {AppObjects}
                template={TemplateList[i]}
              />
            </li>
          {/each}
        </ul>
      </div>
    </div>
  {/if}
</div>

<div
  class="modal fade"
  id="deleteModal"
  tabindex="-1"
  aria-labelledby="exampleModalLabel"
  aria-hidden="true"
>
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-body">
        <p>Are you sure you want to delete this?</p>
      </div>
      <div class="modal-footer">
        <button
          type="button"
          class="btn btn-danger"
          data-bs-dismiss="modal"
          on:click={Func}>Yes</button
        >
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
          >No</button
        >
      </div>
    </div>
  </div>
</div>

<style>
  .liSpecial {
    border: 0 !important;
  }
  .scrollSpecial {
    overflow-y: auto;
    overflow-x: hidden;
    max-height: 65vh;
    margin-bottom: 500px !important;
  }
</style>
