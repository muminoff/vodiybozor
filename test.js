/**
 * Prints below:
 * waited 250
 * resolved to 250
 * waited 500
 * waited 1000
 */

async function test() {
  const promises = [2000, 3000, 1000].map(ms => wait(ms));
  console.log('resolved to', await Promise.race(promises));
}

async function wait(ms) {
  await new Promise(resolve => setTimeout(() => resolve(), ms));
  console.log('waited', ms);
  return ms;
}

async function foo() {
  await new Promise((resolve, reject) => setTimeout(() => resolve(), 1000));
  console.log('Hello, World!');
}

foo();
