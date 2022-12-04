const { readFileSync, promises: fsPromises } = require('fs');

const syncReadFile = (filename) => {
    const contents = readFileSync(filename, 'utf-8');

    const arr = contents.split(/\r?\n/);

    return arr;
}

const priority = (item) => {
    const code = item.charCodeAt(0)
    if (code > 96) return code - 96
    else return code - 64 + 26
}

rucksacks = syncReadFile('./input.txt');

const totalPriorities = rucksacks.map(rucksack => {
    const size = rucksack.length
    leftPocket = rucksack.substr(0, size / 2)
    rightPocket = rucksack.substr(size / 2)

    const reoccurringItems = leftPocket.split('').filter(value => rightPocket.split('').includes(value));
    const priorities = reoccurringItems.map(c => priority(c));
    return priorities[0]
}).reduce((partialSum, prio) => partialSum + prio, 0)

console.log('totalPriorities', totalPriorities)


const computeGroupPriority = (rucksacks) => {
    const groupedSacks = []
    while (rucksacks.length) groupedSacks.push(rucksacks.splice(0, 3));

    return groupedSacks.map(
        groupSacks => {
            const shared01 = groupSacks[0].split('').filter(value => groupSacks[1].split('').includes(value))
            const shared012 = shared01.filter(value => groupSacks[2].split('').includes(value))
            return priority(shared012[0])
        })
        .reduce((partialSum, prio) => partialSum + prio, 0)

}

console.log('group priority', computeGroupPriority(rucksacks))
