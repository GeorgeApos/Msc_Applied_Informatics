const { MongoClient } = require('mongodb');

const uri = 'mongodb://localhost:27017';
const dbName = 'mydatabase';

const runQueries = async (client) => {
    const db = client.db(dbName);

    try {
        // Query 1: Cities within any distance of each other
        const query1 = await db.collection('poleis').aggregate([
            {
                $geoNear: {
                    near: { type: 'Point', coordinates: [] },
                    distanceField: 'dist.calculated',
                    spherical: true
                }
            },
            {
                $lookup: {
                    from: 'poleis',
                    let: { cityId: '$_id' },
                    pipeline: [
                        {
                            $match: {
                                $expr: {
                                    $and: [
                                        { $lt: ['$_id', '$$cityId'] },
                                        { $eq: ['$geometry.type', 'Point'] }
                                    ]
                                }
                            }
                        },
                        {
                            $geoNear: {
                                near: { type: 'Point', coordinates: [] },
                                distanceField: 'dist.calculated',
                                spherical: true
                            }
                        },
                        {
                            $project: {
                                city1: '$onoma',
                                city2: '$$ROOT.onoma',
                                _id: 0
                            }
                        }
                    ],
                    as: 'pairedCities'
                }
            }
        ]).toArray();
        console.log('Query 1 result:', query1);

        // Query 2: Nomoi intersected by the river Pineios
        const query2 = await db.collection('nomoi').aggregate([
            {
                $lookup: {
                    from: 'potamoi',
                    let: { geom: '$geometry' },
                    pipeline: [
                        {
                            $match: {
                                $expr: {
                                    $and: [
                                        { $eq: ['$geometry.type', 'Point'] },
                                        { $regexMatch: { input: '$name', regex: '^ΠΗΝΕΙΟ' } }
                                    ]
                                }
                            }
                        }
                    ],
                    as: 'potamoi'
                }
            },
            {
                $match: { 'potamoi': { $ne: [] } }
            },
            {
                $group: {
                    _id: '$name_gr'
                }
            }
        ]).toArray();
        console.log('Query 2 result:', query2);

        // Query 3: Lakes located on the boundaries of more than one nomos
        const query3 = await db.collection('limnes').aggregate([
            {
                $lookup: {
                    from: 'nomoi',
                    localField: 'geometry',
                    foreignField: 'geometry',
                    as: 'nomoi'
                }
            },
            {
                $unwind: '$nomoi'
            },
            {
                $group: {
                    _id: '$name',
                    count: { $sum: 1 }
                }
            },
            {
                $match: {
                    count: { $gt: 1 }
                }
            }
        ]).toArray();
        console.log('Query 3 result:', query3);

        // Additional Queries 0a and 0b can be added here similarly
    } catch (err) {
        console.error(err);
    }
};

const main = async () => {
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        await client.connect();
        console.log('Connected to MongoDB');
        await runQueries(client);
    } catch (err) {
        console.error(err);
    } finally {
        await client.close();
        console.log('MongoDB connection closed');
    }
};

main();
