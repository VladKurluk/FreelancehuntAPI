<template>
  <div class="container">
    <div class="columns">
      <div class="column is-11">
        <b-field label="Email"
          type="is-primary"
          message="This email is invalid">
          <b-input type="email"
            value="john@"
            maxlength="30"></b-input>
        </b-field>
      </div>
      <div class="column is-1 has-background-warning">
        <b-button type="is-primary" @click="clickMe">Click Me</b-button>
      </div>
    </div>
  </div>
</template>
