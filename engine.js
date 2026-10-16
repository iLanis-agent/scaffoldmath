// Scaffold Math engine - hypothetical arithmetic on labeled norms only.
// No verdicts about load ratings or safe assembly: what holds weight is the
// manufacturer's rating, and the manual owns guardrails, outriggers and ties.

function plural(n, one, many) { return n === 1 ? one : many; }

function fixed1(x) { return (Math.floor(x * 10 + 0.5) / 10).toFixed(1); }

function platformFeet(claim, person) {
  if (!(claim > 0)) throw new Error("the claimed reach must be above zero");
  if (!(person > 0)) throw new Error("the person norm must be above zero");
  if (!(person < claim)) throw new Error("the person norm must be less than the claimed reach");
  return claim - person;
}

function reachTruth(claim, person) {
  const platform = platformFeet(claim, person);
  let verdict;
  if (platform <= 4) verdict = "a one-level stack honestly";
  else if (platform <= 9) verdict = "a two-level stack honestly";
  else verdict = "a tall stack honestly";
  return `The box claims a ${claim}-foot reach; at the ${person}-foot person norm the platform stands ${fixed1(platform)} ${plural(platform === 1 ? 1 : 0, "foot", "feet")} up - ${verdict}.`;
}

function towerCount(wall, coverage) {
  if (!(wall > 0)) throw new Error("the wall length must be above zero");
  if (!(coverage > 0)) throw new Error("the tower coverage must be above zero");
  return Math.ceil(wall / coverage);
}

function towerTruth(wall, coverage) {
  const towers = towerCount(wall, coverage);
  let verdict;
  if (towers <= 1) verdict = "one tower and done";
  else if (towers <= 3) verdict = "a short row honestly";
  else if (towers <= 8) verdict = "a working row of towers";
  else verdict = "a scaffold-yard honestly";
  return `A ${wall}-foot wall at ${coverage} ${plural(coverage, "foot", "feet")} a tower is ${towers} ${plural(towers, "tower", "towers")} - ${verdict}.`;
}

function plankCount(wall, plank) {
  if (!(wall > 0)) throw new Error("the wall length must be above zero");
  if (!(plank > 0)) throw new Error("the plank length must be above zero");
  return Math.ceil(wall / plank);
}

function plankTruth(wall, plank, levels) {
  if (!(levels > 0)) throw new Error("the level count must be above zero");
  const perLevel = plankCount(wall, plank);
  const total = perLevel * levels;
  let verdict;
  if (total <= 1) verdict = "one plank and done";
  else if (total <= 2) verdict = "a pair of planks honestly";
  else if (total <= 6) verdict = "a stack of planks honestly";
  else if (total <= 16) verdict = "a lumber pile honestly";
  else verdict = "a rental-yard honestly";
  return `A ${wall}-foot wall takes ${perLevel} ${plural(perLevel, "plank", "planks")} of ${plank} feet a level; ${levels} ${plural(levels, "level", "levels")} is ${total} ${plural(total, "plank", "planks")} - ${verdict}.`;
}

if (typeof module !== "undefined") {
  module.exports = { platformFeet, reachTruth, towerCount, towerTruth, plankCount, plankTruth };
}
