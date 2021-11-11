<script>
  // Imports
  import Introduction from "./Components/Introduction.svelte";
  import Template from "./Components/Template.svelte";
  import Output from "./Components/Output.svelte";
  import Load from "./Components/Load.svelte";
  import Cookies from "./Components/Cookies.svelte";
  import { fade, fly } from "svelte/transition";

  // File loads
  let AppObjects = {
    workoutObject: [],
    muscleGroupArray: [],
    exerciseTypeArray: [],
    equipmentArray: [],
    experienceArray: [],
  };

  class ExerciseEntry {
    constructor(MuscleGroups, ExerciseTypes, Equipments, Experience) {
      this.MuscleGroups = MuscleGroups;
      this.ExerciseTypes = ExerciseTypes;
      this.Equipments = Equipments;
      this.Experience = Experience;
    }
  }

  let TemplateList = [];
  let ExerciseList = [];
  // Local variables
  let mode = 0;

  let animationDelay = 200;
  let animationSpeed = 600;
</script>

<body class="bg-white">
  {#if mode == 0}
    <div class="BackgroundImage imageA">
      <img
        class=""
        src="/images/human_a.png"
        alt=""
        in:fly={{
          x: -1 * animationSpeed,
          duration: animationDelay,
          delay: animationDelay,
        }}
        out:fade={{ x: animationSpeed, duration: animationDelay }}
      />
    </div>
  {:else if mode == 1}
    <div class="BackgroundImage imageB">
      <img
        class="img-fluid float-start"
        src="/images/human_b.webp"
        alt=""
        in:fly={{
          x: -1 * animationSpeed,
          duration: animationDelay,
          delay: animationDelay,
        }}
        out:fade={{ x: animationSpeed, duration: animationDelay }}
      />
    </div>
  {:else if mode == 2}
    <div class="BackgroundImage imageC">
      <img
        class="img-fluid"
        src="/images/human_c.webp"
        alt=""
        in:fly={{
          x: animationSpeed,
          duration: animationDelay,
          delay: animationDelay,
        }}
        out:fade={{ x: -1 * animationSpeed, duration: animationDelay }}
      />
    </div>
  {:else}
    <div class="BackgroundImage imageD">
      <img
        class="img-fluid"
        src="/images/human_h.webp"
        alt=""
        in:fly={{
          x: -1 * animationSpeed,
          duration: animationDelay,
          delay: animationDelay,
        }}
        out:fade={{ x: animationSpeed, duration: animationDelay }}
      />
    </div>
  {/if}

  <Load bind:AppObjects />

  <div class="container-fluid shadow">
    <div class="row">
      <nav class="navbar sticky-top navbar-light navbar-expand">
        <div class="container NavbarContainer ">
          <div class="navbar-brand">
            <h1 class="display-6 text-dark">
              AUTO <span class="text-secondary">SETS</span>
            </h1>
          </div>
        </div>
        <div class="col">
          <button
            type="button"
            class="btn btn-outline-secondary shadow-sm"
            on:click={() => {
              mode = mode < 3 ? 3 : 0;
            }}
          >
            {mode < 3 ? "Load" : "Go Back"}
          </button>
        </div>
      </nav>
    </div>
  </div>

  <div class="container Main">
    <div class="row">
      <div class="col-3">
        <button
          type="button"
          class="btn btn-outline-secondary shadow-sm {mode == 0
            ? 'disabled'
            : ''} {mode == 3 ? 'invisible' : ''}"
          on:click={() => {
            mode = Math.max(mode - 1, 0);
            animationSpeed = -1 * Math.abs(animationSpeed);
          }}
        >
          Previous Step
        </button>
      </div>
      <div class="col-6" />
      <div class="col-3">
        <button
          type="button"
          class="btn btn-outline-secondary shadow-sm {mode == 2
            ? 'disabled'
            : ''} {mode == 3 ? 'invisible' : ''}"
          on:click={() => {
            mode = Math.min(mode + 1, 2);
            animationSpeed = Math.abs(animationSpeed);
          }}
        >
          Next Step</button
        >
      </div>
    </div>
    <div class="Component">
      {#if mode == 0}
        <div
          in:fly={{
            x: animationSpeed,
            duration: animationDelay,
            delay: animationDelay,
          }}
          out:fly={{ x: -1 * animationSpeed, duration: animationDelay }}
        >
          <Introduction />
        </div>
      {:else if mode == 1}
        <div
          in:fly={{
            x: animationSpeed,
            duration: animationDelay,
            delay: animationDelay,
          }}
          out:fly={{ x: -1 * animationSpeed, duration: animationDelay }}
        >
          <Template bind:AppObjects bind:TemplateList />
        </div>
      {:else if mode == 2}
        <div
          in:fly={{
            x: animationSpeed,
            duration: animationDelay,
            delay: animationDelay,
          }}
          out:fly={{ x: -1 * animationSpeed, duration: animationDelay }}
        >
          <Output bind:AppObjects bind:TemplateList bind:ExerciseList />
        </div>
      {:else}
        <div
          in:fly={{
            x: animationSpeed,
            duration: animationDelay,
            delay: animationDelay,
          }}
          out:fly={{ x: -1 * animationSpeed, duration: animationDelay }}
        >
          <Cookies bind:AppObjects />
        </div>
      {/if}
    </div>

    <div class="specialFooter">
      <nav class="navbar fixed-bottom navbar-light">
        <div class="col-12">
          <div class="navbar-text text-center">
            {#if mode == 0}
              <div
                in:fly={{
                  x: animationSpeed,
                  duration: animationDelay,
                  delay: animationDelay,
                }}
              >
                <h5>Welcome!</h5>
              </div>
            {:else if mode == 1}
              <div
                in:fly={{
                  x: animationSpeed,
                  duration: animationDelay,
                  delay: animationDelay,
                }}
              >
                <h5>Select your workout!!</h5>
              </div>
            {:else if mode == 2}
              <div
                in:fly={{
                  x: animationSpeed,
                  duration: animationDelay,
                  delay: animationDelay,
                }}
              >
                <h5>Now do your best!</h5>
              </div>
            {:else}
              <div
                in:fly={{
                  x: animationSpeed,
                  duration: animationDelay,
                  delay: animationDelay,
                }}
              >
                <h5>Load your favourite workouts!</h5>
              </div>
            {/if}
          </div>
        </div>
      </nav>
    </div>
  </div>
</body>

<style>
  body {
    max-width: 100%;
    overflow-x: hidden;
    overflow-y: hidden;
    z-index: 3;
  }
  .Main {
    text-align: center;
    padding: 2%;
  }
  .NavbarContainer {
    margin-left: 2%;
  }
  .BackgroundImage {
    position: absolute;
    overflow: hidden;
    z-index: 0;
    pointer-events: none;
  }
  .BackgroundImage > img {
    height: 100;
    opacity: 16%;
  }
  .imageA {
    float:right !important;
    clear: right !important;
    left:0%;
    margin-left: 5em;
    scale: 150%;
    margin-top: 12em;
  }
  .imageB {
    left: 10%;
    margin-left: 2em;
    margin-top: 1em;
  }
  .imageC {
    margin-left: 30%;
  }
  .imageD {
    left: 10%;
    margin-bottom: 15%;
  }
  .specialFooter {
    pointer-events: none;
  }
</style>
